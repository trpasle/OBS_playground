Name:       hello-world
Version:    1
Release:    1
Summary:    Most simple RPM package
License:    FIXME
Source:     hello.sh

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
