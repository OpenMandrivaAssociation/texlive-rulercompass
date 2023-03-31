Name:		texlive-rulercompass
Version:	32392
Release:	2
Summary:	A TikZ library for straight-edge and compass diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/rulercompass
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rulercompass.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rulercompass.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rulercompass.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
