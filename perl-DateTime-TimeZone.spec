#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DateTime-TimeZone
Version  : 1.93
Release  : 12
URL      : http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/DateTime-TimeZone-1.93.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/DateTime-TimeZone-1.93.tar.gz
Summary  : 'Time zone object base class and factory'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-DateTime-TimeZone-doc
BuildRequires : perl(Class::Singleton)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Params::Validate)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::More)
BuildRequires : perl(Test::Output)
BuildRequires : perl(Test::Requires)
BuildRequires : perl(Test::Taint)
BuildRequires : perl(Try::Tiny)

%description
NAME
DateTime::TimeZone - Time zone object base class and factory
VERSION
version 1.93

%package doc
Summary: doc components for the perl-DateTime-TimeZone package.
Group: Documentation

%description doc
doc components for the perl-DateTime-TimeZone package.


%prep
%setup -q -n DateTime-TimeZone-1.93

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/Abidjan.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/Accra.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/Algiers.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/Bissau.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/Cairo.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/Casablanca.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/Ceuta.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/El_Aaiun.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/Johannesburg.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/Khartoum.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/Lagos.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/Maputo.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/Monrovia.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/Nairobi.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/Ndjamena.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/Tripoli.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/Tunis.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Africa/Windhoek.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Adak.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Anchorage.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Araguaina.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Argentina/Buenos_Aires.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Argentina/Catamarca.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Argentina/Cordoba.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Argentina/Jujuy.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Argentina/La_Rioja.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Argentina/Mendoza.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Argentina/Rio_Gallegos.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Argentina/Salta.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Argentina/San_Juan.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Argentina/San_Luis.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Argentina/Tucuman.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Argentina/Ushuaia.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Asuncion.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Atikokan.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Bahia.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Bahia_Banderas.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Barbados.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Belem.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Belize.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Blanc_Sablon.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Boa_Vista.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Bogota.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Boise.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Cambridge_Bay.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Campo_Grande.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Cancun.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Caracas.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Cayenne.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Cayman.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Chicago.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Chihuahua.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Costa_Rica.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Creston.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Cuiaba.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Curacao.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Danmarkshavn.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Dawson.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Dawson_Creek.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Denver.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Detroit.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Edmonton.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Eirunepe.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/El_Salvador.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Fortaleza.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Glace_Bay.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Godthab.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Goose_Bay.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Grand_Turk.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Guatemala.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Guayaquil.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Guyana.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Halifax.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Havana.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Hermosillo.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Indiana/Indianapolis.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Indiana/Knox.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Indiana/Marengo.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Indiana/Petersburg.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Indiana/Tell_City.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Indiana/Vevay.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Indiana/Vincennes.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Indiana/Winamac.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Inuvik.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Iqaluit.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Jamaica.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Juneau.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Kentucky/Louisville.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Kentucky/Monticello.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/La_Paz.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Lima.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Los_Angeles.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Maceio.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Managua.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Manaus.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Martinique.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Matamoros.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Mazatlan.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Menominee.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Merida.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Metlakatla.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Mexico_City.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Miquelon.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Moncton.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Monterrey.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Montevideo.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Nassau.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/New_York.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Nipigon.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Nome.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Noronha.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/North_Dakota/Beulah.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/North_Dakota/Center.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/North_Dakota/New_Salem.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Ojinaga.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Panama.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Pangnirtung.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Paramaribo.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Phoenix.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Port_au_Prince.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Port_of_Spain.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Porto_Velho.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Puerto_Rico.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Rainy_River.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Rankin_Inlet.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Recife.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Regina.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Resolute.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Rio_Branco.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Santa_Isabel.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Santarem.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Santiago.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Santo_Domingo.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Sao_Paulo.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Scoresbysund.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Sitka.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/St_Johns.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Swift_Current.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Tegucigalpa.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Thule.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Thunder_Bay.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Tijuana.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Toronto.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Vancouver.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Whitehorse.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Winnipeg.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Yakutat.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/America/Yellowknife.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Antarctica/Casey.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Antarctica/Davis.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Antarctica/DumontDUrville.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Antarctica/Macquarie.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Antarctica/Mawson.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Antarctica/Palmer.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Antarctica/Rothera.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Antarctica/Syowa.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Antarctica/Troll.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Antarctica/Vostok.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Almaty.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Amman.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Anadyr.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Aqtau.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Aqtobe.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Ashgabat.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Baghdad.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Baku.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Bangkok.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Beirut.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Bishkek.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Brunei.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Chita.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Choibalsan.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Colombo.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Damascus.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Dhaka.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Dili.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Dubai.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Dushanbe.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Gaza.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Hebron.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Ho_Chi_Minh.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Hong_Kong.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Hovd.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Irkutsk.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Jakarta.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Jayapura.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Jerusalem.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Kabul.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Kamchatka.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Karachi.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Kathmandu.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Khandyga.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Kolkata.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Krasnoyarsk.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Kuala_Lumpur.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Kuching.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Macau.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Magadan.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Makassar.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Manila.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Nicosia.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Novokuznetsk.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Novosibirsk.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Omsk.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Oral.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Pontianak.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Pyongyang.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Qatar.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Qyzylorda.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Rangoon.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Riyadh.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Sakhalin.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Samarkand.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Seoul.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Shanghai.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Singapore.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Srednekolymsk.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Taipei.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Tashkent.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Tbilisi.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Tehran.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Thimphu.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Tokyo.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Ulaanbaatar.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Urumqi.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Ust_Nera.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Vladivostok.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Yakutsk.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Yekaterinburg.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Asia/Yerevan.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Atlantic/Azores.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Atlantic/Bermuda.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Atlantic/Canary.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Atlantic/Cape_Verde.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Atlantic/Faroe.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Atlantic/Madeira.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Atlantic/Reykjavik.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Atlantic/South_Georgia.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Atlantic/Stanley.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Australia/Adelaide.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Australia/Brisbane.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Australia/Broken_Hill.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Australia/Currie.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Australia/Darwin.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Australia/Eucla.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Australia/Hobart.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Australia/Lindeman.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Australia/Lord_Howe.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Australia/Melbourne.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Australia/Perth.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Australia/Sydney.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/CET.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/CST6CDT.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Catalog.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/EET.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/EST.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/EST5EDT.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Amsterdam.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Andorra.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Athens.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Belgrade.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Berlin.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Brussels.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Bucharest.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Budapest.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Chisinau.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Copenhagen.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Dublin.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Gibraltar.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Helsinki.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Istanbul.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Kaliningrad.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Kiev.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Lisbon.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/London.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Luxembourg.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Madrid.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Malta.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Minsk.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Monaco.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Moscow.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Oslo.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Paris.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Prague.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Riga.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Rome.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Samara.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Simferopol.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Sofia.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Stockholm.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Tallinn.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Tirane.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Uzhgorod.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Vienna.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Vilnius.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Volgograd.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Warsaw.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Zaporozhye.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Europe/Zurich.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Floating.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/HST.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Indian/Chagos.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Indian/Christmas.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Indian/Cocos.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Indian/Kerguelen.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Indian/Mahe.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Indian/Maldives.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Indian/Mauritius.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Indian/Reunion.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Local.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Local/Android.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Local/Unix.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Local/VMS.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/MET.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/MST.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/MST7MDT.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/OffsetOnly.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/OlsonDB.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/OlsonDB/Change.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/OlsonDB/Observance.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/OlsonDB/Rule.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/OlsonDB/Zone.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/PST8PDT.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Apia.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Auckland.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Bougainville.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Chatham.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Chuuk.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Easter.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Efate.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Enderbury.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Fakaofo.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Fiji.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Funafuti.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Galapagos.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Gambier.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Guadalcanal.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Guam.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Honolulu.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Kiritimati.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Kosrae.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Kwajalein.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Majuro.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Marquesas.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Nauru.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Niue.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Norfolk.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Noumea.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Pago_Pago.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Palau.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Pitcairn.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Pohnpei.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Port_Moresby.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Rarotonga.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Tahiti.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Tarawa.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Tongatapu.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Wake.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/Pacific/Wallis.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/UTC.pm
/usr/lib/perl5/site_perl/5.22.0/DateTime/TimeZone/WET.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
