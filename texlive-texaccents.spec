%global tl_name texaccents
%global tl_revision 64447
%global tl_bin_links texaccents:%{_texmfdistdir}/scripts/texaccents/texaccents.sno

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	Convert composite accented characters to Unicode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/texaccents
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texaccents.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texaccents.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texaccents.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(texaccents.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
This small utility, written in SNOBOL, converts the composition of
special characters to Unicode, e. g. \"{a} - a, \k{a} - a, ...

