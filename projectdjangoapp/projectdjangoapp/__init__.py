#https://stackoverflow.com/questions/55657752/django-installing-mysqlclient-error-mysqlclient-1-3-13-or-newer-is-required
import pymysql
pymysql.version_info = (1, 4, 6, 'final', 0)
pymysql.install_as_MySQLdb()