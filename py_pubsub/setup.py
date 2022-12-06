from setuptools import setup

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ivan',
    maintainer_email='nazgoool1@gmail.com',
    description='Package description',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot_control_pub = py_pubsub.pub_robot_move_control:main',
            'laser_take = py_pubsub.laser_sensor_get:main',
            'robot_control_sub = py_pubsub.sub_robot_move_control:main',
        ],
    },
)
