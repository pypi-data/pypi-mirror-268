#!/bin/bash

set -e
set -o pipefail

BUILD_DIR="pybuild"
if [ ! -d "$BUILD_DIR" ]; then
  mkdir "$BUILD_DIR"
  pushd "$BUILD_DIR"
  cmake ../.. -DCMAKE_BUILD_TYPE=Debug -DRTPIV_PYTHON=ON -G Ninja
  popd
fi

cmake --build "$BUILD_DIR"

# PLATLIB="$(python -c 'import sysconfig;print(sysconfig.get_paths()["platlib"])')"
PLATLIB='/home/user/.local/lib/python3.12/site-packages'
echo 'copying .so'
SO_LIBRARY=("${BUILD_DIR}"/src/_core.*.so)
SO_NAME="$(basename "${SO_LIBRARY[0]}")"
if [ ! -f "${PLATLIB}/rtpiv/${SO_NAME}" ]; then
  echo "could not find ${SO_NAME} in existing install"
  exit 1
fi
cp "${SO_LIBRARY[0]}" "${PLATLIB}/rtpiv/"

echo 'copying __init__.py'
cp ../src/rtpiv/__init__.py "${PLATLIB}/rtpiv/"