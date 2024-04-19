import json
from pathlib import Path
from warnings import warn
import torch
from torch.utils.data import Dataset, DataLoader, get_worker_info
from smart_open import smart_open, parse_uri
from torch.multiprocessing import Manager
# from torch.utils.data.datapipes.iter import S3FileLoader
# import torchdata
import boto3
# import ray.data

# ray.data.read_binary_files
# ray.data.read_binary_files


class ShardedDataset(Dataset):
    def __init__(self):
        self.index = ray.data.read_json('s3://ai-residency-stanford-snap-uce/datasets/data_taxon/index.json')
    
    def __iter__(self):
        worker_info = get_worker_info()

        if worker_info is None:
            worker_id = 0
            num_workers = 1
        else:
            worker_id = worker_info.id
            num_workers = worker_info.num_workers
            assert num_workers == 1
        return self
    
    def __next__(self):
        pass



# s3 = boto3.client('s3')

# class ShardedDataset(Dataset):
#     def __init__(self, dataset_dir: Path | str):
#         dataset_dir = Path(dataset_dir)

#         with open(dataset_dir / 'index.json', 'r') as f:
#             self.index = json.load(f)
    
#     def __iter__(self):
#         worker_info = get_worker_info()
#         if worker_info is None:
#             worker_id = 0
#             num_workers = 1
#         else:
#             worker_id = worker_info.id
#             num_workers = worker_info.num_workers



# def cached_read(maybe_remote_dir, local_dir=None):
#     """
#     Get the local path for a possibly remote file, downloading it if necessary, and loading cached local files.
#     """
#     uri = parse_uri(maybe_remote_dir)
#     if uri.scheme == 's3':
#         if local_dir is None:
#             warn('Using temporary cache directory in /tmp')
#         remote_path = uri.key_id
#         key_id = uri.key_id
#         bucket_id = uri.bucket_id
#         print(f'{bucket_id=} {key_id=}')
#         o = s3.get_object(Bucket=bucket_id, Key=key_id)
#         s3_last_modified = o['LastModified']
#         print(s3_last_modified)

#         if local_dir is None:
#             local_dir = f'/tmp/{remote_path}'
        
#         local_dir = Path(local_dir)

#         if not local_dir.parent.exists():
#             local_dir.parent.mkdir(parents=True)
        
#         if local_dir.exists():  # File already downloaded
#             local_last_modified = local_dir.stat().st_mtime
#             if s3_last_modified.timestamp() > local_last_modified:
#                 print(f'Downloading {key_id} to {local_dir}')
#                 s3.download_file(bucket_id, key_id, local_dir)
#             return local_dir
        
#         s3.download_file(bucket_id, key_id, local_dir)

#         # s3.download_file(bucket_id, key_id, local_dir)
#         return local_dir

#     elif uri.scheme == 'file':
#         if local_dir is not None:
#             warn('Ignoring local_dir for local file caching')
#         return uri.uri_path
#     else:
#         raise ValueError(f'Unsupported scheme: {uri.scheme}. Raise an issue on GitHub if you need this.')




if __name__ == '__main__':
    # cached_read('s3://ai-residency-stanford-snap-uce/datasets/data_taxon/protein_shuffled_val.blosc.pkl', None)
    cached_read('/tmp/file', None)