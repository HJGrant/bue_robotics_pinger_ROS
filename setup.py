from setuptools import find_packages, setup

package_name = 'blue_robotics_pinger'

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
    maintainer='hamish',
    maintainer_email='hamish.grant@tum.de',
    description='ROS Packages for BlueROV Pinger',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pinger_publisher_node = blue_robotics_pinger.pinger_publisher_node:main',
            'pinger_subscriber_node = blue_robotics_pinger.pinger_subscriber_node:main',
        ],
    },
)
