# revision 30458
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-context
Epoch:		1
Version:	20131013
Release:	1
Summary:	ConTeXt and packages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-context.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-context
Requires:	texlive-collection-basic
Requires:	texlive-jmn
Requires:	texlive-context-account
Requires:	texlive-context-algorithmic
Requires:	texlive-context-bnf
Requires:	texlive-context-chromato
Requires:	texlive-context-construction-plan
Requires:	texlive-context-cyrillicnumbers
Requires:	texlive-context-degrade
Requires:	texlive-context-filter
Requires:	texlive-context-fixme
Requires:	texlive-context-french
Requires:	texlive-context-fullpage
Requires:	texlive-context-games
Requires:	texlive-context-gantt
Requires:	texlive-context-gnuplot
Requires:	texlive-context-letter
Requires:	texlive-context-lettrine
Requires:	texlive-context-lilypond
Requires:	texlive-context-mathsets
Requires:	texlive-context-notes-zh-cn
Requires:	texlive-context-rst
Requires:	texlive-context-ruby
Requires:	texlive-context-simplefonts
Requires:	texlive-context-simpleslides
Requires:	texlive-context-transliterator
Requires:	texlive-context-typearea
Requires:	texlive-context-typescripts
Requires:	texlive-context-vim

%description
Hans Hagen's powerful ConTeXt system, http://pragma-ade.com.
Also includes third-party ConTeXt packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
