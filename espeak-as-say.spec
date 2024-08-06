Name:           espeak-as-say
Version:        1.0.3
Release:        2%{?dist}
License:        MIT
Summary:        Installs a script in /usr/bin/say that calls espeak        
Url:            https://github.com/dkolb/%{name}
Source0:        %{name}-%{version}.tar.gz

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
* Tue Aug 06 2024 David Kolb <git@dkub.dev> 1.0.3-2
- build: fix bad reference in spec (git@dkub.dev)

* Tue Aug 06 2024 David Kolb <git@dkub.dev>
- build: fix bad reference in spec (git@dkub.dev)

* Tue Aug 06 2024 David Kolb <git@dkub.dev>
- build: fix bad reference in spec (git@dkub.dev)

* Tue Aug 06 2024 David Kolb <git@dkub.dev> 1.0.3-1
- Automatic commit of package [espeak-as-say] release [1.0.2-1]. (git@dkub.dev)

* Tue Aug 06 2024 David Kolb <git@dkub.dev>
- 

* Tue Aug 06 2024 David Kolb <git@dkub.dev>
- testing keep-version 

* Tue Aug 06 2024 David Kolb <git@dkub.dev> 1.0.2-1
- try again (git@dkub.dev)

* Tue Aug 06 2024 David Kolb <git@dkub.dev>
- try again (git@dkub.dev)

* Tue Aug 06 2024 David Kolb <git@dkub.dev>
- fix bad source (maybe?) (git@dkub.dev)

* Tue Aug 06 2024 David Kolb <git@dkub.dev> 1.0.1-1
- cleanup: remove some bs. (git@dkub.dev)

* Tue Aug 06 2024 David Kolb <git@dkub.dev> 1.0.0-1
- new package built with tito
- inital builds
* Tue Aug 06 2024 David Kolb <git@dkub.dev>
- 
