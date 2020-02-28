from __future__ import print_function

import tensorflow as tf
import sys

MINIMUM_TF_VERSION = 1, 14, 0
BLACKLISTED_TF_VERSIONS = [
    (2, 0, 0),  # Has a number of memory leaks and issues with eager execution.
    (2, 0, 1),  # Has a number of memory leaks and issues with eager execution.
]


def tf_version():
    """ Get the Tensorflow version.
        Returns
            tuple of (major, minor, patch).
    """
    return tuple(map(int, tf.version.VERSION.split('-')[0].split('.')))


def tf_version_ok(minimum_tf_version=MINIMUM_TF_VERSION, blacklisted=BLACKLISTED_TF_VERSIONS):
    """ Check if the current Tensorflow version is higher than the minimum version.
    """
    return tf_version() >= minimum_tf_version and tf_version() not in blacklisted


def assert_tf_version(minimum_tf_version=MINIMUM_TF_VERSION, blacklisted=BLACKLISTED_TF_VERSIONS):
    """ Assert that the Tensorflow version is up to date.
    """
    detected = tf.version.VERSION
    required = '.'.join(map(str, minimum_tf_version))
    assert(tf_version_ok(minimum_tf_version, blacklisted)), 'You are using tensorflow version {}. The minimum required version is {} (blacklisted: {}).'.format(detected, required, blacklisted)


def check_tf_version():
    """ Check that the Tensorflow version is up to date. If it isn't, print an error message and exit the script.
    """
    try:
        assert_tf_version()
    except AssertionError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
