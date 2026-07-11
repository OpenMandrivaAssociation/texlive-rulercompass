%global tl_name rulercompass
%global tl_revision 32392

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1
Release:	%{tl_revision}.1
Summary:	A TikZ library for straight-edge and compass diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/rulercompass
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rulercompass.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rulercompass.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rulercompass.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines some commands and styles to support drawing
straight-edge and compass diagrams with TikZ.

