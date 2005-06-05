%define		_name	MinionWeb
Summary:	Adobe Minion Web - part of Adobe WebType
Summary(pl):	Font Adobe Minion Web - czê¶æ Adobe WebType
Name:		fonts-TTF-Adobe-%{_name}
Version:	1.0
Release:	1
License:	nondistributable on term of Internet Explorer 4 EULA
Group:		Fonts
Source0:	http://maxtor1.slu.edu.ph/Public/GRAPHICS/Photodlx/INSTALL/IE4/FONTSUP.CAB
# NoSource0-md5:	64e173b3b6fac1ff9105c361308baee4
NoSource:	0
BuildRequires:	cabextract
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         ttffontsdir     %{_fontsdir}/TTF

%description
Minion is an Adobe Originals typeface family designed by Robert
Slimbach. Minion is inspired by classical, old style typefaces of the
late Renaissance, a period of elegant, beautiful, and highly readable
type designs. Minion Web has been optimized for onscreen use.

%description -l pl
Minion to rodzina rodzina krojów pisma Adobe Originals zaprojektowana
przez Roberta Slimbacha. Minion zosta³ zainspirowany klasycznymi
krojami pisma w starym stylu z pó¼nego renesansu - okresu eleganckich,
piêknych i bardzo czytelnych wzorów czcionek. Minion Web zosta³
zoptymalizowany do u¿ywania na ekranie.

%prep
%setup -q -T -c
cabextract %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install Minionw.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{ttffontsdir}/*.ttf
