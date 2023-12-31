# Generated by Django 4.1.7 on 2023-06-05 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0002_barang_waktu_posting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jenis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('ket', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='barang',
            name='jenis_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produk.jenis'),
        ),
    ]
