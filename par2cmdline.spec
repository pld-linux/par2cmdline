Summary:	PAR 2.0 compatible file verification and repair tool
Summary(pl.UTF-8):	Narzędzie do weryfikacji i naprawiania plików zgodne z PAR 2.0
Name:		par2cmdline
Version:	0.4
Release:	3
License:	GPL v2+
Group:		Applications/Archiving
Source0:	http://dl.sourceforge.net/parchive/%{name}-%{version}.tar.gz
# Source0-md5:	1551b63e57e3c232254dc62073b723a9
Patch0:		%{name}-fix-crash-in-quiet-mode.patch
Patch1:		%{name}-gcc41.patch
URL:		http://sourceforge.net/projects/parchive/
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
par2cmdline is a program for creating and using PAR2 files to detect
damage in data files and repair them if necessary. It can be used with
any kind of file.

%description -l pl.UTF-8
par2cmdline to program do tworzenia i używania plików PAR2 do
wykrywania uszkodzeń w plikach z danymi i naprawiania ich w razie
potrzeby. Może być używany na dowolnych rodzajach plików.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* .
%configure

%{__make} all check

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
