1205�汾
1. ���b�Ŀ�h�� 
   1.1 ���bpython3.5+�汾����� 
   1.2 ���bVirtualenv����춄���̓�M�h���İ���
   1.3 ���Ŀ���b��̨�h�� python35 -m Virtualenv edgebox_final(�h����)
   1.4 �����Ŀ�h�� cd edgebox_final/Scripts   .activate
   1.5 �x�����b��ه�� python -m pip install --no-index -f ./whls(�x����λ��) -r pkg.txt(����) 
2. ���ӭh��
   2.1 �����Ŀ�h�� cd edgebox_final/Scripts   .activate
   2.2 ����Django python manage.py runserver 0.0.0.0:8002(�˿�Ŀǰ�cVueһ��8002)
   2.3 ����celery�΄� python manage.py celeryd -l info 
   2.4 ����celery���r�΄� python manage.py celerybeat -l info ������������Ҳ����work ,���M5ģ�K��
3. �����Ŀ�h�� (δ��Ҫ)
   3.1 �����Ŀ�h�� cd edgebox_final/Scripts   .activate
   3.2 ʹ��pip�����������Ŀ��ه�� pip freeze ->pkg.txt
   3.3 ʹ��pip�������ھ����d�Ŀ��ه�� pip download -r pkg.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
