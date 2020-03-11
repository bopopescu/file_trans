# Generated by Django 2.2.6 on 2019-10-02 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('gateway_name', models.CharField(max_length=30, verbose_name='网关唯一名称')),
                ('gateway_key', models.CharField(max_length=100, verbose_name='网关id')),
                ('gateway_secret', models.CharField(max_length=200, verbose_name='网关秘钥')),
                ('gateway_tokenapi', models.CharField(max_length=200, verbose_name='网关鉴权URl')),
                ('gateway_subdevice_num', models.IntegerField(default=0, verbose_name='网关子设备数量')),
                ('gateway_model', models.CharField(max_length=30, verbose_name='网关型号')),
                ('gateway_trade_name', models.CharField(max_length=30, verbose_name='网关厂商名称')),
                ('gateway_registration_time', models.DateTimeField(verbose_name='网关注册时间')),
                ('gateway_location', models.CharField(max_length=30, verbose_name='网关位置信息')),
                ('gateway_remark', models.CharField(max_length=50, verbose_name='网关描述')),
            ],
            options={
                'db_table': 'gateway_register_info',
                'verbose_name_plural': '网关产品注册信息',
                'verbose_name': '网关产品注册信息',
            },
        ),
    ]