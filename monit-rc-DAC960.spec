Summary:	monitrc file for monitoring DAC960 status
Summary(pl.UTF-8):	Plik monitrc do monitorowania stanu DAC960
Name:		monit-rc-DAC960
Version:	3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	DAC960.monitrc
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	monit
Requires:	monit
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
monitrc file for monitoring DAC960 status.

%description -l pl.UTF-8
Plik monitrc do monitorowania stanu DAC960.

%prep

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
