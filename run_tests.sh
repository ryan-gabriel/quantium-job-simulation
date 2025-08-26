#!/bin/bash
set -e

source venv/Scripts/activate

pytest

if [ $? -eq 0 ]; then
  echo "✅ All tests passed!"
  exit 0
else
  echo "❌ Some tests failed!"
  exit 1
fi
