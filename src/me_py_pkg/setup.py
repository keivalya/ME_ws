from setuptools import find_packages, setup

package_name = 'me_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kv',
    maintainer_email='kv@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node = me_py_pkg.my_first_node:main",
            "robot_news_station = me_py_pkg.robot_news_station:main",
            "smartphone = me_py_pkg.smartphone:main"
        ],
    },
)
