# RPM Spec file
# Martin Iturbide

Name:           LX2Dump
Version:        1.03
Release:        1%{?dist}
Summary:        Linear eXecutable Dump Facility/2 Utility.
Group:          Utility
License:        BSD Alike
          

Vendor:         Stangl Roman

Obsoletes:	LX2Dump < %{version}-%{release}
Provides:	LX2Dump = %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	i686


%description
LX2Dump is a utility to extract information from executable files. 

%prep
# we have no source, so nothing here

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/@unixroot/usr/bin
mkdir -p $RPM_BUILD_ROOT/@unixroot/usr/share/doc/%{name}
cp -p LX2Dump.exe $RPM_BUILD_ROOT/@unixroot/usr/bin
cp -p BuildLevel.cmd $RPM_BUILD_ROOT/@unixroot/usr/bin
cp -p LX2Dump.txt $RPM_BUILD_ROOT/@unixroot/usr/share/doc/%{name}

%files
%{_bindir}/LX2Dump.exe
%{_bindir}/BuildLevel.cmd
%doc LX2Dump.txt

%changelog
# let's skip this for now