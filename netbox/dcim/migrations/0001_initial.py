# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 18:21
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import utilities.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsolePort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('connection_status', models.NullBooleanField(choices=[[False, b'Planned'], [True, b'Connected']], default=True)),
            ],
            options={
                'ordering': ['device', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ConsolePortTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['device_type', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ConsoleServerPort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ConsoleServerPortTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['device_type', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', utilities.fields.NullableCharField(blank=True, max_length=50, null=True, unique=True)),
                ('serial', models.CharField(blank=True, max_length=50, verbose_name=b'Serial number')),
                ('position', models.PositiveSmallIntegerField(blank=True, help_text=b'Number of the lowest U position occupied by the device', null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name=b'Position (U)')),
                ('face', models.PositiveSmallIntegerField(blank=True, choices=[[0, b'Front'], [1, b'Rear']], null=True, verbose_name=b'Rack face')),
                ('status', models.BooleanField(choices=[[True, b'Active'], [False, b'Offline']], default=True, verbose_name=b'Status')),
                ('comments', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DeviceRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('color', models.CharField(choices=[[b'teal', b'Teal'], [b'green', b'Green'], [b'blue', b'Blue'], [b'purple', b'Purple'], [b'yellow', b'Yellow'], [b'orange', b'Orange'], [b'red', b'Red'], [b'light_gray', b'Light Gray'], [b'medium_gray', b'Medium Gray'], [b'dark_gray', b'Dark Gray']], max_length=30)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('u_height', models.PositiveSmallIntegerField(default=1, verbose_name=b'Height (U)')),
                ('is_full_depth', models.BooleanField(default=True, help_text=b'Device consumes both front and rear rack faces', verbose_name=b'Is full depth')),
                ('is_console_server', models.BooleanField(default=False, help_text=b'This type of device has console server ports', verbose_name=b'Is a console server')),
                ('is_pdu', models.BooleanField(default=False, help_text=b'This type of device has power outlets', verbose_name=b'Is a PDU')),
                ('is_network_device', models.BooleanField(default=True, help_text=b'This type of device has network interfaces', verbose_name=b'Is a network device')),
            ],
            options={
                'ordering': ['manufacturer', 'model'],
            },
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('form_factor', models.PositiveSmallIntegerField(choices=[[0, b'Virtual'], [800, b'10/100M (Copper)'], [1000, b'1GE (Copper)'], [1100, b'1GE (SFP)'], [1200, b'10GE (SFP+)'], [1300, b'10GE (XFP)'], [1400, b'40GE (QSFP+)']], default=1200)),
                ('mgmt_only', models.BooleanField(default=False, help_text=b'This interface is used only for out-of-band management', verbose_name=b'OOB Management')),
                ('description', models.CharField(blank=True, max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interfaces', to='dcim.Device')),
            ],
            options={
                'ordering': ['device', 'name'],
            },
        ),
        migrations.CreateModel(
            name='InterfaceConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection_status', models.BooleanField(choices=[[False, b'Planned'], [True, b'Connected']], default=True, verbose_name=b'Status')),
                ('interface_a', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='connected_as_a', to='dcim.Interface')),
                ('interface_b', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='connected_as_b', to='dcim.Interface')),
            ],
        ),
        migrations.CreateModel(
            name='InterfaceTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('form_factor', models.PositiveSmallIntegerField(choices=[[0, b'Virtual'], [800, b'10/100M (Copper)'], [1000, b'1GE (Copper)'], [1100, b'1GE (SFP)'], [1200, b'10GE (SFP+)'], [1300, b'10GE (XFP)'], [1400, b'40GE (QSFP+)']], default=1200)),
                ('mgmt_only', models.BooleanField(default=False, verbose_name=b'Management only')),
                ('device_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interface_templates', to='dcim.DeviceType')),
            ],
            options={
                'ordering': ['device_type', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('part_id', models.CharField(blank=True, max_length=50, verbose_name=b'Part ID')),
                ('serial', models.CharField(blank=True, max_length=50, verbose_name=b'Serial number')),
                ('discovered', models.BooleanField(default=False, verbose_name=b'Discovered')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='dcim.Device')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submodules', to='dcim.Module')),
            ],
            options={
                'ordering': ['device__id', 'parent__id', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('rpc_client', models.CharField(blank=True, choices=[[b'juniper-junos', b'Juniper Junos (NETCONF)'], [b'cisco-ios', b'Cisco IOS (SSH)'], [b'opengear', b'Opengear (SSH)']], max_length=30, verbose_name=b'RPC client')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PowerOutlet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='power_outlets', to='dcim.Device')),
            ],
        ),
        migrations.CreateModel(
            name='PowerOutletTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('device_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='power_outlet_templates', to='dcim.DeviceType')),
            ],
            options={
                'ordering': ['device_type', 'name'],
            },
        ),
        migrations.CreateModel(
            name='PowerPort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('connection_status', models.NullBooleanField(choices=[[False, b'Planned'], [True, b'Connected']], default=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='power_ports', to='dcim.Device')),
                ('power_outlet', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='connected_port', to='dcim.PowerOutlet')),
            ],
            options={
                'ordering': ['device', 'name'],
            },
        ),
        migrations.CreateModel(
            name='PowerPortTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('device_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='power_port_templates', to='dcim.DeviceType')),
            ],
            options={
                'ordering': ['device_type', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('facility_id', utilities.fields.NullableCharField(blank=True, max_length=30, null=True, verbose_name=b'Facility ID')),
                ('u_height', models.PositiveSmallIntegerField(default=42, verbose_name=b'Height (U)')),
                ('comments', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['site', 'name'],
            },
        ),
        migrations.CreateModel(
            name='RackGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['site', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('facility', models.CharField(blank=True, max_length=50)),
                ('asn', models.PositiveIntegerField(blank=True, null=True, verbose_name=b'ASN')),
                ('physical_address', models.CharField(blank=True, max_length=200)),
                ('shipping_address', models.CharField(blank=True, max_length=200)),
                ('comments', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='rackgroup',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rack_groups', to='dcim.Site'),
        ),
        migrations.AddField(
            model_name='rack',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='racks', to='dcim.RackGroup'),
        ),
        migrations.AddField(
            model_name='rack',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='racks', to='dcim.Site'),
        ),
        migrations.AddField(
            model_name='devicetype',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='device_types', to='dcim.Manufacturer'),
        ),
        migrations.AddField(
            model_name='device',
            name='device_role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='devices', to='dcim.DeviceRole'),
        ),
        migrations.AddField(
            model_name='device',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='instances', to='dcim.DeviceType'),
        ),
        migrations.AddField(
            model_name='device',
            name='platform',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='devices', to='dcim.Platform'),
        ),
    ]
