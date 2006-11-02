Summary:	monitrc file for monitoring DAC960 status
Name:		monit-rc-DAC960
Version:	3
Release:	1
License:	GPL
Group:		Applications
Source0:	DAC960.monitrc
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	monit
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
monitrc file for monitoring DAC960 status.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/monit
install %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/monit

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q monit restart

%postun
%service -q monit restart

%files
%defattr(644,root,root,755)
%{_sysconfdir}/monit/*.monitrc
