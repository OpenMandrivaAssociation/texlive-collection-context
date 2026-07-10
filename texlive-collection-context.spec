%global tl_name collection-context
%global tl_revision 75426

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	ConTeXt and packages
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-context
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-context.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(collection-basic)
Requires:	texlive(context)
Requires:	texlive(context-animation)
Requires:	texlive(context-calendar-examples)
Requires:	texlive(context-chat)
Requires:	texlive(context-collating-marks)
Requires:	texlive(context-cyrillicnumbers)
Requires:	texlive(context-filter)
Requires:	texlive(context-gnuplot)
Requires:	texlive(context-handlecsv)
Requires:	texlive(context-legacy)
Requires:	texlive(context-letter)
Requires:	texlive(context-mathsets)
Requires:	texlive(context-notes-zh-cn)
Requires:	texlive(context-pocketdiary)
Requires:	texlive(context-simpleslides)
Requires:	texlive(context-squares)
Requires:	texlive(context-sudoku)
Requires:	texlive(context-transliterator)
Requires:	texlive(context-typescripts)
Requires:	texlive(context-vim)
Requires:	texlive(context-visualcounter)
Requires:	texlive(jmn)
Requires:	texlive(luajittex)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hans Hagen's powerful ConTeXt system, https://pragma-ade.com. Also
includes third-party ConTeXt packages. TeX Live uses the ConTeXt
repackaging as distributed from https://github.com/gucci-on-
fleek/context-packaging. See https://contextgarden.net and
https://pragma-ade.com for information about ConTeXt.#

