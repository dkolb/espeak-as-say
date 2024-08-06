Name:           espeak-as-say
Version:        1.0.1
Release:        %autorelease
Summary:        Installs a script in /usr/bin/say that calls espeak        

License:        MIT
URL:            https://github.com/dkolb/%{name}
Source0:        %\{name}-%\{src_version}.tar.gz

#BuildRequires:
Requires:       espeak
Requires:       bash

%description
Installs a bash script /usr/bin/say that calls espeak instead

%prep
%autosetup

%install 
install -d %{buildroot}/usr/bin
install say %{buildroot}/usr/bin/say

%files
%license LICENSE
/usr/bin/say
%doc README.md AUTHORS



%changelog
* Tue Aug 06 2024 David Kolb <git@dkub.dev> 1.0.1-1
- cleanup: remove some bs. (git@dkub.dev)

* Tue Aug 06 2024 David Kolb <git@dkub.dev> 1.0.0-1
- new package built with tito
- inital builds
* Tue Aug 06 2024 David Kolb <git@dkub.dev>
- 
