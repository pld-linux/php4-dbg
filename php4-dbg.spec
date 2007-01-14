#
# INFO: How to get working: patching, installation, using with PHPeclipse (*very* helpful):
#	http://www.phpeclipse.de/tiki-view_forum_thread.php?forumId=3&comments_parentId=3265
#
Summary:	dbg - PHP debbuger - extension for PHP 4
Summary(pl):	dbg - debugger dla PHP - rozszerzenie PHP 4
Name:		php4-dbg
Version:	2.11.32
Release:	0.2
License:	The DBG License Version 3.0
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/dbg2/dbg-%{version}-src.tar.gz
# Source0-md5:	1ac7372bfcb4c5e13cad1248e071d70c
Source1:	dbg.ini
URL:		http://dd.cron.ru/dbg/
BuildRequires:	rpmbuild(macros) >= 1.344
BuildRequires:	php4-devel >= 3:4.0.0
%{?requires_php_extension}
Requires:	php4-common >= 3:4.4.0-3
Obsoletes:	dbg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBG is a a full-featured php debugger, an interactive tool that helps
you debugging php scripts. It works on a production and/or development
WEB server and allows you debug your scripts locally or remotely, from
an IDE or console. This package contain dbg extension for PHP 4.

%description -l pl
DBG to w pe³ni funkcjonalny debugger dla PHP - interaktywne narzêdzie
pomagaj±ce przy diagnostyce skryptów w PHP. Dzia³a zarówno na
produkcyjnym jak i rozwojowym serwerze WWW, pozwala na ¶ledzenie
skryptów lokalnie jak i zdalnie, z poziomu IDE lub konsoli. Ten pakiet
zawiera rozszerzenie dbg dla PHP 4.

%prep
%setup -q -n dbg-%{version}

%build
phpize
%configure \
	--with-dbg-profiler \
	--enable-dbg=shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d
install %{SOURCE1} $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/dbg.ini

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php4_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php4_webserver_restart
fi

%files
%defattr(644,root,root,755)
# don't remove COPYING and INSTALL
%doc AUTHORS COPYING INSTALL
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/dbg.ini
%attr(755,root,root) %{php_extensiondir}/dbg.so
