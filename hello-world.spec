Name:       OBS_playground
Version:    main
Release:    2
Summary:    Most simple RPM package
License:    FIXME
Source:     OBS_playground-%{version}.tar

%description

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/bin/
install -m 700 hello.sh %{buildroot}/usr/bin/hello.sh

%files
/usr/bin/hello.sh
