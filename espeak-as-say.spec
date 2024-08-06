# x-release-please-start-version
%define src_version 1.0.0
# x-release-please-end

Name:           espeak-as-say
Version:        %{src_version}
Release:        %autorelease
Summary:        Installs a script in /usr/bin/say that calls espeak        

License:        MIT
URL:            https://github.com/dkolb/%{name}
Source0:        https://github.com/dkolb/%{name}/%{name}-%{src_version}.tar.gz

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
* Tue Aug 06 2024 David Kolb <git@dkub.dev>
- 
