#!/bin/sh
set -e

# 1) 마이그레이션
python manage.py migrate --noinput

# 2) 정적파일(필요 시)
python manage.py collectstatic --noinput

# 3) 애플리케이션 실행 (전달된 명령 실행)
exec "$@"
