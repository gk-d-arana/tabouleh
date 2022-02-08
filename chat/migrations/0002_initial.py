# Generated by Django 3.2.6 on 2022-02-08 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_roles', '0001_initial'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryoperatorchatroom',
            name='admin_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adminchatdeliveryoperator', to='user_roles.admin'),
        ),
        migrations.AddField(
            model_name='deliveryoperatorchatroom',
            name='delivery_operator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_roles.deliveryoperator'),
        ),
        migrations.AddField(
            model_name='customerchatroom',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adminchatcustomer', to='user_roles.admin'),
        ),
        migrations.AddField(
            model_name='customerchatroom',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_roles.customer'),
        ),
    ]