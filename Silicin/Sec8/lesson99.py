import tarfile

with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    # tr.extractall(path='test_tar')
    with tr.extractfile('test_dir/test.txt') as f:
        print(f.read())