from setuptools import setup

package_name = 'simple_pub_sub'

setup(
    name=package_name,
    version='0.0.1',
    packages=['simple_pub_sub'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Simple Publisher and Subscriber example for ROS 2 Humble',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = First_package.publisher:main',
            'subscriber = First_package.subscriber:main',
        ],
    },
)
