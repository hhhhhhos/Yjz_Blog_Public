import os

# �����ػ�����
daemon=True
# ���������˿�8000
bind='0.0.0.0:8000'
# ���ý����ļ�Ŀ¼
pidfile='./gunicorn.pid'
chdir='./' # ����Ŀ¼
# ����ģʽ
worker_class='uvicorn.workers.UvicornWorker'
# ���й��������� ������*2+1��
workers=3  #multiprocessing.cpu_count()+1
# ָ��ÿ�������ߵ��߳���
threads=2
# ������󲢷���
worker_connections = 200
loglevel='debug' # ������־����־����
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
# ���÷�����־�ʹ�����Ϣ��־·��
log_dir = "./log"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
accesslog = "./log/gunicorn_access.log"
errorlog = "./log/gunicorn_error.log"