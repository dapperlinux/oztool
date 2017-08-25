Summary:    Graphical Oz Profile Editor
Name:       oztool
Version:    1
Release:    2

Group:      System Environment/Base
License:    GPLV3
Url:        https://github.com/shw700/oztool
Source0:    %{name}-%{version}.tar.xz
BuildArch:  x86_64

BuildRequires:  go
Requires:   cairo-gobject
BuildRequires:  cairo-gobject-devel
BuildRequires:  gtk3-devel
BuildRequires:  git
Requires:   dapper-oz-profiles


%description
Oztool is a graphical editor for Oz profiles. Oztool enables you to create and 
modify existing profiles, and enables you to easily add whitelisted and blacklisted 
paths on sandboxes.

%prep
%autosetup

%build
mkdir -p %{_builddir}/gocode/src/github.com/subgraph/
mv oztool %{_builddir}/gocode/src/github.com/subgraph/
export GOPATH=%{_builddir}/gocode
go get -tags gtk_3_20 github.com/gotk3/gotk3/gtk
go build -tags gtk_3_20 github.com/subgraph/oztool


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datarootdir}/applications
install -m 755 oztool %{buildroot}%{_bindir}
cp %{_builddir}/gocode/src/github.com/subgraph/oztool/oztool.desktop %{buildroot}%{_datarootdir}/applications


%clean

%pre

%post

%files
%{_bindir}/oztool
%{_datarootdir}/applications/oztool.desktop

%changelog
* Sat Apr  8 2017 Matthew Ruffell <msr50@uclive.ac.nz>
- First packaging
