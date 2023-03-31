Name:		texlive-texaccents
Version:	64447
Release:	2
Summary:	Convert composite accented characters to Unicode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texaccents
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texaccents.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texaccents.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texaccents.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small utility, written in SNOBOL, converts the composition
of special characters to Unicode, e. g. \"{a} - a, \k{a} - a,
...

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/texmf-dist/source/support/texaccents
%{_texmfdistdir}/texmf-dist/scripts/texaccents
%doc %{_texmfdistdir}/texmf-dist/doc/support/texaccents
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/texaccents.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/texaccents.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
