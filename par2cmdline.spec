Summary:	PAR 2.0 compatible file verification and repair tool
Summary(pl):	Narzêdzie do weryfikacji i naprawiania plików zgodne z PAR 2.0
Name:		par2cmdline
Version:	0.4
Release:	1
License:	GPL v2+
Group:		Applications/Archiving
Source0:	http://dl.sourceforge.net/parchive/%{name}-%{version}.tar.gz
# Source0-md5:	1551b63e57e3c232254dc62073b723a9
URL:		http://sourceforge.net/projects/parchive/
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
par2cmdline is a program for creating and using PAR2 files to detect
damage in data files and repair them if necessary. It can be used with
any kind of file.

%description -l pl
par2cmdline to program do tworzenia i u¿ywania plików PAR2 do
wykrywania uszkodzeñ w plikach z danymi i naprawiania ich w razie
potrzeby. Mo¿e byæ u¿ywany na dowolnych rodzajach plików.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf par2 $RPM_BUILD_ROOT%{_bindir}/par

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/par
%attr(755,root,root) %{_bindir}/par2*
