Summary:	PAR 2.0 compatible file verification and repair tool
Name:		par2cmdline
Version:	0.3
Release:	1
License:	GPL v2+
Group:		Applications/Archiving
Source0:	http://dl.sourceforge.net/parchive/%{name}-%{version}.tar.gz
# Source0-md5:	705c97bc41b862d281dd41c219a60849
URL:		http://sourceforge.net/projects/parchive
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
par2cmdline is a program for creating and using PAR2 files to detect
damage in data files and repair them if necessary. It can be used with
any kind of file.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" ./configure --prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
ln -sf %{_bindir}/par2 $RPM_BUILD_ROOT/%{_bindir}/par

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog PORTING README ROADMAP
%attr(755,root,root) %{_bindir}/par
%attr(755,root,root) %{_bindir}/par2
