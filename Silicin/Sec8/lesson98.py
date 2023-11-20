import os
import pathlib
import glob
import shutil

print(os.path.exists('test.txt'))
print(os.path.isfile('test.txt'))
print(os.path.isdir('test.txt'))
print(os.path.isdir('../Sec8'))

# os.rename('test.txt', 'renamed.txt')
# symlinkの中身を書き換えるとリンク先も等しく書き換わる
# os.symlink('renamed.txt', 'symlink.txt')

# os.mkdir('test_dir')
# os.rmdir('test_dir')

# pathlib.Path('empty.txt').touch()
# os.remove('empty.txt')

# os.mkdir('test_dir')
# # os.mkdir('test_dir/test_dir2')
# os.mkdir('test_dir/test_dir2')
# pathlib.Path('test_dir/test_dir2/empty.txt').touch()
# print(os.listdir('test_dir'))
# shutil.copy('test_dir/test_dir2/empty.txt', 'test_dir/test_dir2/empty2.txt')
# print(glob.glob('test_dir/test_dir2/*'))

# shutil.rmtree('test_dir')
# print(os.getcwd())