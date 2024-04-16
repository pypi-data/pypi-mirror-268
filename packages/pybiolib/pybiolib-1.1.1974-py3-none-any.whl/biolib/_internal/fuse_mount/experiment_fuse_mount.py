import errno
import os
import stat
from datetime import datetime, timezone
from time import time
from typing import Iterable

from biolib._internal.libs.fusepy import FUSE, FuseOSError, Operations
from biolib.biolib_errors import BioLibError
from biolib.jobs import Job
from biolib.typing_utils import Dict, Optional, Tuple, TypedDict


class _AttributeDict(TypedDict):
    st_atime: int
    st_ctime: int
    st_gid: int
    st_mode: int
    st_mtime: int
    st_nlink: int
    st_size: int
    st_uid: int


class ExperimentFuseMount(Operations):
    def __init__(self, experiment):
        self._experiment = experiment
        self._job_names_map: Optional[Dict[str, Job]] = None
        self._jobs_last_fetched_at: float = 0.0
        self._root_path: str = '/'
        self._mounted_at_epoch_seconds: int = int(time())

    @staticmethod
    def mount(experiment, path: str) -> None:
        FUSE(
            operations=ExperimentFuseMount(experiment),
            mountpoint=path,
            nothreads=True,
            foreground=True,
            allow_other=False,
        )

    def getattr(self, path: str, fh=None) -> _AttributeDict:
        full_path = self._full_path(path)
        if full_path == '/':
            # return folder dir
            return self._get_folder_attr(timestamp_epoch_seconds=self._mounted_at_epoch_seconds)

        job_name, job_path = self._parse_path(path)
        job = self._get_job_names_map().get(job_name)
        if not job:
            # job not found
            raise FuseOSError(errno.ENOENT)

        job_finished_at_epoch_seconds: int = int(
            datetime.fromisoformat(job.to_dict()['finished_at'].rstrip('Z')).replace(tzinfo=timezone.utc).timestamp()
        )
        if not job_path or job_path == '/':
            # job root path
            return self._get_folder_attr(timestamp_epoch_seconds=job_finished_at_epoch_seconds)

        try:
            file = job.get_output_file(job_path)
        except BioLibError:
            # file not found
            raise FuseOSError(errno.ENOENT) from None

        return _AttributeDict(
            st_atime=job_finished_at_epoch_seconds,
            st_ctime=job_finished_at_epoch_seconds,
            st_gid=os.getgid(),
            st_mode=stat.S_IFREG | 0o444,  # Regular file with read permissions for owner, group, and others.
            st_mtime=job_finished_at_epoch_seconds,
            st_nlink=1,
            st_size=file.length,
            st_uid=os.getuid(),
        )

    def readdir(self, path: str, fh: int) -> Iterable[str]:
        directory_entries = ['.', '..']
        if path == '/':
            for name in self._get_job_names_map(refresh_jobs=True):
                directory_entries.append(name)
        else:
            job_name, job_path = self._parse_path(path)
            job = self._get_job_names_map()[job_name]
            in_target_directory = set(
                [k.path.split('/')[1] for k in job.list_output_files() if k.path.startswith(job_path)]
            )

            for key in in_target_directory:
                directory_entries.append(key)

        yield from directory_entries

    def open(self, path: str, flags: int) -> int:
        job_name, job_path = self._parse_path(path)
        job = self._get_job_names_map()[job_name]
        try:
            job.get_output_file(job_path)
            return 0  # return dummy file handle
        except BioLibError:
            # file not found
            raise FuseOSError(errno.ENOENT) from None

    def read(self, path: str, size: int, offset: int, fh: int) -> bytes:
        job_name, job_path = self._parse_path(path)
        job = self._get_job_names_map()[job_name]
        try:
            file = job.get_output_file(job_path)
        except BioLibError:
            # file not found
            raise FuseOSError(errno.ENOENT) from None

        return file.get_data(start=offset, length=size)

    def _get_folder_attr(self, timestamp_epoch_seconds: int) -> _AttributeDict:
        return _AttributeDict(
            st_atime=timestamp_epoch_seconds,
            st_ctime=timestamp_epoch_seconds,
            st_gid=os.getgid(),
            st_mode=stat.S_IFDIR | 0o555,  # Directory that is readable and executable by owner, group, and others.
            st_mtime=timestamp_epoch_seconds,
            st_nlink=1,
            st_size=1,
            st_uid=os.getuid(),
        )

    def _get_job_names_map(self, refresh_jobs=False) -> Dict[str, Job]:
        current_time = time()
        if not self._job_names_map or (current_time - self._jobs_last_fetched_at > 1 and refresh_jobs):
            self._jobs_last_fetched_at = current_time
            self._job_names_map = {job.get_name(): job for job in self._experiment.get_jobs(status='completed')}

        return self._job_names_map

    def _full_path(self, partial: str) -> str:
        if partial.startswith('/'):
            partial = partial[1:]

        return os.path.join(self._root_path, partial)

    def _parse_path(self, path: str) -> Tuple[str, str]:
        full_path = self._full_path(path)
        full_path_splitted = full_path.split('/')
        job_name = full_path_splitted[1]
        job_path = '/'.join(full_path_splitted[2:])
        return job_name, job_path

    # ----------------------------------- File system methods not implemented below -----------------------------------

    def chmod(self, path, mode):
        raise FuseOSError(errno.EACCES)

    def chown(self, path, uid, gid):
        raise FuseOSError(errno.EACCES)

    def mknod(self, path, mode, dev):
        raise FuseOSError(errno.EACCES)

    def rmdir(self, path):
        raise FuseOSError(errno.EACCES)

    def mkdir(self, path, mode):
        raise FuseOSError(errno.EACCES)

    def unlink(self, path):
        raise FuseOSError(errno.EACCES)

    def symlink(self, target, source):
        raise FuseOSError(errno.EACCES)

    def rename(self, old, new):
        raise FuseOSError(errno.EACCES)

    def link(self, target, source):
        raise FuseOSError(errno.EACCES)

    def utimens(self, path, times=None):
        raise FuseOSError(errno.EACCES)

    def create(self, path, mode, fi=None):
        raise FuseOSError(errno.EACCES)

    def write(self, path, data, offset, fh):
        raise FuseOSError(errno.EACCES)

    def truncate(self, path, length, fh=None):
        raise FuseOSError(errno.EACCES)

    def flush(self, path, fh):
        raise FuseOSError(errno.EACCES)

    def release(self, path, fh):
        raise FuseOSError(errno.EACCES)

    def fsync(self, path, datasync, fh):
        raise FuseOSError(errno.EACCES)
