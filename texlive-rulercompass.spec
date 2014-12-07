# revision 32392
# category Package
# catalog-ctan /graphics/pgf/contrib/rulercompass
# catalog-date 2013-12-11 23:41:59 +0100
# catalog-license lppl1.3
# catalog-version 1
Name:		texlive-rulercompass
Version:	1
Release:	4
Summary:	A TikZ library for straight-edge and compass diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/rulercompass
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rulercompass.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rulercompass.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rulercompass.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines some commands and styles to support drawing
straight-edge and compass diagrams with TikZ.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rulercompass/tikzlibraryrulercompass.code.tex
%doc %{_texmfdistdir}/doc/latex/rulercompass/README.txt
%doc %{_texmfdistdir}/doc/latex/rulercompass/rulercompass.pdf
%doc %{_texmfdistdir}/doc/latex/rulercompass/rulercompass_doc.pdf
%doc %{_texmfdistdir}/doc/latex/rulercompass/rulercompass_doc.tex
#- source
%doc %{_texmfdistdir}/source/latex/rulercompass/rulercompass.dtx
%doc %{_texmfdistdir}/source/latex/rulercompass/rulercompass.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
