# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-18 19:25
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packagedb', '0008_package_package_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='DependentPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purl', models.CharField(blank=True, help_text='A compact purl package URL', max_length=2048, null=True)),
                ('requirement', models.CharField(blank=True, help_text='A string defining version(s)requirements. Package-type specific.', max_length=200, null=True)),
                ('scope', models.CharField(blank=True, help_text='The scope of this dependency, such as runtime, install, etc. This is package-type specific and is the original scope string.', max_length=100, null=True)),
                ('is_runtime', models.BooleanField(default=True, help_text='True if this dependency is a runtime dependency.')),
                ('is_optional', models.BooleanField(default=False, help_text='True if this dependency is an optional dependency')),
                ('is_resolved', models.BooleanField(default=False, help_text='True if this dependency version requirement has been resolved and this dependency url points to an exact version.')),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('person', 'person'), ('project', 'project'), ('organization', 'organization')], help_text='the type of this party', max_length=20, null=True)),
                ('role', models.CharField(blank=True, help_text='A role for this party. Something such as author, maintainer, contributor, owner, packager, distributor, vendor, developer, owner, etc.', max_length=32, null=True)),
                ('name', models.CharField(blank=True, help_text='Name of this party.', max_length=70, null=True)),
                ('email', models.CharField(blank=True, help_text='Email for this party.', max_length=255, null=True)),
                ('url', models.CharField(blank=True, help_text='URL to a primary web page for this party.', max_length=1024, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='package',
            name='metadata',
        ),
        migrations.AddField(
            model_name='package',
            name='bug_tracking_url',
            field=models.CharField(blank=True, help_text='URL to the issue or bug tracker for this package', max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='code_type',
            field=models.CharField(blank=True, help_text='Primary type of code in this Package such as source, binary, data, documentation.', max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='code_view_url',
            field=models.CharField(blank=True, help_text='a URL where the code can be browsed online', max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='copyright',
            field=models.TextField(blank=True, help_text='Copyright statements for this package. Typically one per line.', null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='declared_licensing',
            field=models.CharField(blank=True, help_text='The licensing text as declared in a package manifest.', max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='description',
            field=models.TextField(blank=True, help_text='Description for this package. By convention the first line should be a summary when available.', null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='download_checksums',
            field=models.TextField(blank=True, help_text='A list of checksums for this download in hexadecimal and prefixed by the lowercased checksum algorithm and a colon one per line e.g. sha1:c5095691347bd5ad3b5e180238c3914d16f05812', null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='download_url',
            field=models.CharField(blank=True, help_text='A direct download URL.', max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='homepage_url',
            field=models.CharField(blank=True, help_text='URL to the homepage for this package.', max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='keywords',
            field=models.TextField(blank=True, help_text='A list of keywords, one per line.', null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='license_expression',
            field=models.CharField(blank=True, help_text='The license expression for this package.', max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='name',
            field=models.CharField(blank=True, help_text='Name of the package.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='namespace',
            field=models.CharField(blank=True, help_text='Optional namespace for this package.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='notice_text',
            field=models.TextField(blank=True, help_text='A notice text for this package.', null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='primary_language',
            field=models.CharField(blank=True, help_text='Primary programming language', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='qualifiers',
            field=models.CharField(blank=True, help_text='Optional mapping of key=value pairs qualifiers for this package', max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='subpath',
            field=models.CharField(blank=True, help_text='Optional extra subpath inside a package and relative to the root of this package', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='type',
            field=models.CharField(blank=True, help_text='Optional. A short code to identify what is the type of this package. For instance gem for a Rubygem, docker for container, pypi for Python Wheel or Egg, maven for a Maven Jar, deb for a Debian package, etc.', max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='vcs_repository',
            field=models.CharField(blank=True, help_text='a URL to the VCS repository in the SPDX form of:git+https://github.com/nexb/scancode-toolkit.git', max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='vcs_revision',
            field=models.CharField(blank=True, help_text='a revision, commit, branch or tag reference, etc. (can also be included in the URL)', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='vcs_tool',
            field=models.CharField(blank=True, choices=[('git', 'git'), ('svn', 'subversion'), ('hg', 'mercurial'), ('bzr', 'bazaar'), ('cvs', 'cvs')], default='', help_text='The type of VCS tool for this package.', max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='version',
            field=models.CharField(blank=True, help_text='Optional version of the package as a string.', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='package_url',
            field=models.CharField(blank=True, db_index=True, help_text='Package URL for this package. It stands for a package "mostly universal" URL.', max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='party',
            name='package',
            field=models.ForeignKey(help_text='The Package that this party is related to', on_delete=django.db.models.deletion.CASCADE, related_name='parties', to='packagedb.Package'),
        ),
        migrations.AddField(
            model_name='dependentpackage',
            name='package',
            field=models.ForeignKey(help_text='The Package that this dependent package is related to', on_delete=django.db.models.deletion.CASCADE, related_name='dependencies', to='packagedb.Package'),
        ),
    ]