Name:       OBS_playground
Version:    main
Release:    1
Summary:    Most simple RPM package
License:    FIXME
Source:     OBS_playground-1+git.tar

%description

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 hello.sh %{buildroot}/usr/bin/hello.sh

%files
/usr/bin/hello.sh

%changelog
