
%define plugin	podcatcher
%define name	vdr-plugin-%plugin
%define version	0.1.1
%define rel	11

Summary:	VDR plugin: subscribe to podcasts
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.e-tobi.net/blog/pages/vdr-podcatcher
Source:		http://www.e-tobi.net/blog/files/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
BuildRequires:	libcurl-devel
BuildRequires:	libmad-devel
BuildRequires:	libxml++-devel
Requires:	vdr-abi = %vdr_abi

%description
With the Podcatcher plugin you can subscribe to podcasts. It allows you
to browse through the podcasts, download and play them.

%prep
%setup -q -n %plugin-%version

%vdr_plugin_params_begin %plugin
# Specify the cache dir, where the xml feeds and mp3's get cached
var=CACHE_DIR
param=--cache=CACHE_DIR
default=%{_vdr_plugin_cachedir}/%{plugin}
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_cachedir}/%{plugin}
install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}

install -m644 examples/* %{buildroot}%{_vdr_plugin_cfgdir}

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%attr(-,vdr,vdr) %dir %{_vdr_plugin_cachedir}/%{plugin}
%config(noreplace) %{_vdr_plugin_cfgdir}/podcatchersources.conf


