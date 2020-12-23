#
# pipが読んでライブラリの諸々を設定するためのファイル
#
import glob
import setuptools

setuptools.setup(
    name="ProcessObsever",
    version="0.1.0",
    license="MIT Licence",
    description="Process Observing modules",
    author="Enchan1207",
    url="https://github.com/Enchan1207/ProcessObserving",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob.glob('src/*.py')],
    include_package_data=True,
    zip_safe=False
)
