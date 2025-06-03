Name:       hello-world
Version:    1
Release:    1
Summary:    Most simple RPM package
License:    FIXME
Source:     hello.sh

%description
This is my first RPM package, which does nothing.

%prep
# we have no source, so nothing here

%build

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 hello.sh %{buildroot}/usr/bin/hello.sh

%files
/usr/bin/hello.sh
