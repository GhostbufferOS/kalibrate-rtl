%global git_commit aae11c8a8dc79692a94ccfee39ba01e8c8c05d38
%global git_date 20141008
%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:             kalibrate-rtl
URL:              http://github.com/steve-m/kalibrate-rtl
Version:          0.4.1
Release:          3.%{git_suffix}%{?dist}
License:          BSD
BuildRequires:    autoconf, automake, rtl-sdr-devel, fftw-devel
BuildRequires:    libusbx-devel
Group:            Applications/Communications
Summary:          GSM based frequency calibration for rtl-sdr
Source0:          https://github.com/steve-m/%{name}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz


%description
Kalibrate, or kal, can scan for GSM base stations in a given frequency band and
can use those GSM base stations to calculate the local oscillator frequency
offset.

%prep
%setup -qn %{name}-%{git_commit}
autoreconf -fi

%build
%configure
make CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}" %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Rename kal to kal-rtl to avoid possible conflicts
mv %{buildroot}%{_bindir}/kal %{buildroot}%{_bindir}/kal-rtl

%files
%doc COPYING README AUTHORS
%{_bindir}/*

%changelog
* Tue Oct 14 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.1-3.20141008gitaae11c8a
- required libusbx-devel instead of libusb-devel

* Fri Oct 10 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.1-2.20141008gitaae11c8a
- Fixed source URL according to fedora review

* Wed Oct  8 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.1-1.20141008gitaae11c8a
- Initial release
