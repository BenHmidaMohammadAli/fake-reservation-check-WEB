from django.forms import ModelForm
from django import forms
from authentication.models import Passenger
from .models import Flight, ReservationFlight
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ))
    
    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ))
    
    email = forms.EmailField(
        widget= forms.EmailInput(
            attrs={
                "placeholder": "Adress mail",
                "class": "form-control"
                
            }
        ))
    password1 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "placeholder": "Password ",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "placeholder": "Check Password",
                "class": "form-control"
            }
        ))
    
    class Meta:
        model = User
        fields = ['username', 'first_name' ,'last_name' ,'email', 'password1', 'password2']
  

class CreatePassengerForm (ModelForm):

    name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control",
                "readonly": True
            }
        ))
    
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control",
                "readonly": True

            }
        ))
    
    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control",
                "readonly": True
            }
        ))
    
    phone = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Phone",
                "class": "form-control"
            }
        ))
    
    email = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Mail Adress",
                "class": "form-control",
                "readonly": True
            }
        ))
    
    adress = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Adress",
                "class": "form-control"
            }
        ))
    
    class Meta:
        model = Passenger
        fields = ['name', 'first_name' , 'last_name' , 'phone', 'email', 'adress']
        

class CreateFlightForm (ModelForm):
    flight_UID = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Flight UID",
                "class": "form-control",
            }
        ))
    flight_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Flight Name",
                "class": "form-control",
            }
        ))
           
    flight_start = forms.DateTimeField(
        widget= forms.DateTimeInput(
            attrs={
                "placeholder": "Flight start day",
                "class": "form-control" ,
                "type" : "datetime-local"
            }
        )#,input_formats=['%Y-%m-%d %H:%M:%S']
        )
   
    flight_end = forms.DateTimeField(
        widget= forms.DateTimeInput(
            attrs={
                "placeholder": "Flight end day",
                "class" : "form-control" ,
                "type" : "datetime-local"
                }
        )#,input_formats=['%Y-%m-%d %H:%M:%S']
        )

    From = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "From",
                "class": "form-control",
            }
        ))
    To = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "To",
                "class": "form-control",
            }
        ))
    ROUTE_CHOICES =['JOGPER', 'LGKSYD', 'TPETWU', 'HGHSYD', 'TGGXIY', 'DMKOOL', 'KTMMFM', 'MELSZX', 'PVGSGN', 'CKGKCH', 'LOPOOL', 'MAATPE', 'KIXMYY', 'MELMNL', 'RGNTPE', 'CSXMRU', 'DPSHND', 'HKTOOL', 'MELMLE', 'BLRMEL', 'MLETPE', 'REPSYD', 'KBVXIY', 'CTUREP', 'IKAPER', 'PVGURT', 'CNXDEL', 'OOLPEK', 'HGHTGG', 'HNDLGK', 'HNDMLE', 'IKAKCH', 'HGHJHB', 'CCUTPE', 'KBROOL', 'BWNDEL', 'CMBPVG', 'PNHSYD', 'BKIPER', 'CKGOOL', 'CKGPEN', 'DELOOL', 'COKICN', 'CTSSBW', 'DMKIKA', 'HGHMAA', 'DMKMEL', 'MELPNH', 'HDYHGH', 'AKLKUL', 'MAAOOL', 'KHHPER', 'LGKOOL', 'PERREP', 'PVGSYD', 'KNOPEK', 'KNOWUH', 'MAAWUH', 'PERSDK', 'LGKPVG', 'MELMFM', 'REPTPE', 'KBRWUH', 'HNDSIN', 'HDYSYD', 'ICNKTM', 'OOLSZX', 'CTSOOL', 'HGHPEN', 'KIXSGN', 'AKLICN', 'IKAMNL', 'MFMPER', 'HKTWUH', 'GOISYD', 'MRUSIN', 'SYDTRZ', 'BWNPER', 'HGHJOG', 'BKICTU', 'KBVPUS', 'KCHKTM', 'HDYXIY', 'CGKCTS', 'JEDSUB', 'COKPUS', 'BKIMEL', 'CEBSYD', 'HDYKTM', 'KIXKTM', 'KBVPEK', 'HGHLGK', 'CMBICN', 'SBWSYD', 'BDOSYD', 'CMBCTU', 'DELHKG', 'OOLSUB', 'MELRGN', 'DPSMEL', 'DACPUS', 'KNOSYD', 'PENPER', 'SYDSZX', 'CANOOL', 'KIXPEN', 'MLESYD', 'DELPER', 'BWNOOL', 'PENPVG', 'HGHMYY', 'HKGMEL', 'DELSUB', 'JEDPDG', 'KTMMYY', 'BDOHGH', 'CKGLOP', 'DELKNO', 'CMBKIX', 'CTUSIN', 'CMBMEL', 'BDOWUH', 'MELSUB', 'CANDEL', 'ICNSBW', 'HNDKBV', 'SINXIY', 'HANKTM', 'HKTXIY', 'ICNVTZ', 'JHBTPE', 'PNKTPE', 'DELKBR', 'KHHOOL', 'PERUTP', 'MRUXIY', 'KIXPER', 'CMBCTS', 'ICNJED', 'KBVTPE', 'BTUCKG', 'CTUMAA', 'LOPXIY', 'PENPUS', 'DELSIN', 'TWUWUH', 'CKGPER', 'KBVMEL', 'PEKTRZ', 'ICNMYY', 'CGKHND', 'KBVSYD', 'DPSOOL', 'CTUMYY', 'CKGHKT', 'HKGJED', 'PVGRGN', 'PERPUS', 'MFMOOL', 'KBRPUS', 'BWNWUH', 'ICNMLE', 'BBISYD', 'SBWTPE', 'MELNRT', 'CKGMAA', 'CNXPUS', 'TPEURT', 'DPSMRU', 'SYDXIY', 'CKGSIN', 'HNDSUB', 'KLOMEL', 'AORPUS', 'BKIMRU', 'HNDJOG', 'CANPER', 'AKLKIX', 'AORKTM', 'CGKPUS', 'IKAPVG', 'CTULOP', 'LOPPER', 'CTUKBR', 'ICNKBR', 'KTMREP', 'OOLSDK', 'HKTPUS', 'KOSOOL', 'CGKCTU', 'COKSYD', 'PEKSGN', 'BKICTS', 'BTUWUH', 'HKTHND', 'DELREP', 'MRUSGN', 'BOMOOL', 'KIXPNH', 'MAAMRU', 'OOLPEN', 'HKTPEK', 'LGKXIY', 'OOLRGN', 'CNXMEL', 'BDOIKA', 'ICNRGN', 'CKGSGN', 'HNDKCH', 'CGKKIX', 'KBRPEK', 'PERTRZ', 'RGNSYD', 'LPQMEL', 'SUBTPE', 'TPEVTE', 'HKGKTM', 'BLRPER', 'DELMNL', 'KTMTGG', 'MNLPER', 'HGHSIN', 'OOLTWU', 'ICNSUB', 'HNDRGN', 'BWNCKG', 'CTSSYD', 'KBVKIX', 'IKASZX', 'CGKPEK', 'DPSWUH', 'PEKTWU', 'SDKSYD', 'CKGSUB', 'DACICN', 'BTJJED', 'CMBOOL', 'KOSMEL', 'DACOOL', 'HGHPER', 'JHBKTM', 'BBIPER', 'KIXTWU', 'HANSYD', 'COKOOL', 'LGKPUS', 'JOGOOL', 'KNOTPE', 'GOIPER', 'JEDMFM', 'MNLMRU', 'BKIKIX', 'BKICKG', 'LOPSYD', 'MYYPUS', 'PVGREP', 'JEDJOG', 'HKTMEL', 'KBRMEL', 'CNXICN', 'MELXIY', 'CKGMYY', 'PERPVG', 'BLRSYD', 'BTUICN', 'PERSGN', 'BDOTPE', 'CNXOOL', 'KTMSGN', 'KIXTRZ', 'CTUURT', 'DELMRU', 'DACKIX', 'JHBPEK', 'DELLGK', 'HKTSYD', 'CNXPVG', 'HDYKIX', 'BBIMEL', 'CMBSYD', 'HNDLOP', 'HNDMAA', 'TWUXIY', 'LGKMEL', 'CGKKTM', 'SGNSYD', 'CTUPER', 'JHBPUS', 'JOGSYD', 'CTSHKT', 'DMKPEK', 'PERVTZ', 'JHBOOL', 'ICNPER', 'DACPEK', 'MRUTPE', 'KIXTGG', 'CCUOOL', 'CKGSBW', 'HKTMRU', 'CTUIKA', 'DADSYD', 'KCHPUS', 'BWNKTM', 'CRKSYD', 'ICNMRU', 'MELSWA', 'DPSKIX', 'KIXMAA', 'BOMMEL', 'SINSYD', 'CANSYD', 'HDYTPE', 'HGHKBV', 'NRTSYD', 'CKGCOK', 'ICNLGK', 'DACMEL', 'PUSSIN', 'MAASYD', 'CNXHND', 'KTMSYD', 'IKASIN', 'CRKMEL', 'BDOPER', 'BWNTPE', 'LOPPEK', 'MFMSYD', 'PERSWA', 'CTUMLE', 'OOLTRZ', 'BDOMEL', 'KTMSIN', 'KBVWUH', 'LGKWUH', 'CMBPEK', 'HNDREP', 'BWNMEL', 'CTSSIN', 'BWNIKA', 'DELMEL', 'KTMSUB', 'JEDMNL', 'KCHPVG', 'KBVKTM', 'OOLSBW', 'BBIOOL', 'CNXXIY', 'CTSSGN', 'HYDMEL', 'PUSRGN', 'HDYOOL', 'DPSPVG', 'BDOCTU', 'KTMPEN', 'PVGSUB', 'MYYOOL', 'KCHOOL', 'AORMEL', 'KHHSYD', 'KCHPEK', 'KTMTPE', 'MELMYY', 'LPQOOL', 'BKIPUS', 'CTSMYY', 'IKALOP', 'CANIKA', 'DMKMRU', 'BKIPVG', 'IKAOOL', 'PENSYD', 'HGHTWU', 'PVGTWU', 'MLEOOL', 'BLRICN', 'DPSPUS', 'ICNKCH', 'CTUDMK', 'LPQPER', 'CKGMEL', 'DMKKTM', 'KBRPVG', 'SBWXIY', 'HNDOOL', 'LBUTPE', 'OOLVTE', 'PERTGG', 'AKLPVG', 'CTSDMK', 'BDOOOL', 'COKTPE', 'DADMEL', 'ICNPEN', 'CKGJHB', 'BKIDEL', 'DELURT', 'MELSBW', 'JHBMRU', 'SDKTPE', 'MAAPER', 'OOLXIY', 'KBVOOL', 'MAAMEL', 'HKTPER', 'PEKSUB', 'CTUKBV', 'TRZWUH', 'BOMSYD', 'PEKPEN', 'CNXSYD', 'BDOPEK', 'HANMEL', 'CMBWUH', 'MRUSUB', 'ICNREP', 'MELURT', 'JOGPVG', 'HANPER', 'CTUSRG', 'PUSSGN', 'URTXIY', 'KIXRGN', 'AKLDEL', 'KBRPER', 'CTSJOG', 'CTSPER', 'MELTPE', 'CGKPER', 'BDOXIY', 'CTSMEL', 'CTSPEN', 'KBVPER', 'KTMMEL', 'AKLHND', 'ICNMEL', 'MELPUS', 'PEKPER', 'CKGTRZ', 'JOGMEL', 'CGKPVG', 'CGKOOL', 'ICNSGN', 'AKLTPE', 'KNOPVG', 'CGKMRU', 'IKASYD', 'CRKOOL', 'HKGPER', 'HDYPVG', 'MELPEK', 'CSXSYD', 'CTSLGK', 'HKTKIX', 'ICNSIN', 'KBRTPE', 'HKGIKA', 'CMBHND', 'KIXOOL', 'IKAMFM', 'HKTKTM', 'DELRGN', 'DPSSYD', 'COKCTS', 'SYDTWU', 'KCHSYD', 'JHBKIX', 'IKAKIX', 'DELSGN', 'PERPNH', 'DELPNH', 'HDYPEK', 'KIXSIN', 'LGKTPE', 'SRGTPE', 'DACHND', 'KTMURT', 'CKGLGK', 'DELHND', 'KCHXIY', 'DACMRU', 'MELSIN', 'MELTRZ', 'BDOPVG', 'DELDPS', 'DELMFM', 'HNDTRZ', 'BOMPER', 'DPSXIY', 'ICNTGG', 'OOLPUS', 'HNDKTM', 'DACTPE', 'CTUKNO', 'MAAPVG', 'CCUPER', 'KIXSBW', 'KIXLOP', 'OOLSGN', 'HGHSBW', 'TRZXIY', 'HGHLOP', 'HNDSBW', 'KIXREP', 'CEBOOL', 'CTSJHB', 'MELVTZ', 'DPSPEK', 'ICNOOL', 'KLOOOL', 'COKHGH', 'KBRKIX', 'AKLPEK', 'DELPEN', 'DELSYD', 'CTUSUB', 'MNLSYD', 'CTUTGG', 'MELVTE', 'CGKSYD', 'OOLPVG', 'PENXIY', 'HKTJED', 'DELKIX', 'BTUSYD', 'HKGSYD', 'COKPER', 'BDOICN', 'CCUMRU', 'HNDKNO', 'KOSSYD', 'CGKHGH', 'CGKWUH', 'CTUOOL', 'DPSIKA', 'HDYPER', 'DELSZX', 'ICNKNO', 'PERSZX', 'OOLUTP', 'CANMRU', 'KLOSYD', 'DADOOL', 'KIXLGK', 'JEDPEN', 'PERRGN', 'CTUTWU', 'HNDSYD', 'HYDSYD', 'HNDKBR', 'PERVTE', 'DELKBV', 'KNOXIY', 'BDOPUS', 'BKIOOL', 'CTUDPS', 'PUSSBW', 'BWNHGH', 'IKASUB', 'PENTPE', 'CTUTRZ', 'BDOKIX', 'COKMEL', 'AORICN', 'HGHMEL', 'LOPPVG', 'KCHWUH', 'HYDMRU', 'CTUSBW', 'IKAPUS', 'GOIOOL', 'JHBXIY', 'BKIICN', 'OOLSIN', 'DMKPER', 'COKWUH', 'DMKTPE', 'KIXMRU', 'CCUMEL', 'AKLKTM', 'MNLOOL', 'HNDPER', 'HKTPVG', 'COKCTU', 'KIXSYD', 'DELHKT', 'DELDMK', 'HNDSGN', 'KBVPVG', 'TPETRZ', 'CGKIKA', 'CNXPER', 'KNOKTM', 'PUSSUB', 'OOLWUH', 'KWLPER', 'SYDVTZ', 'HKGOOL', 'HYDPER', 'MELTWU', 'SUBWUH', 'JHBWUH', 'KCHKIX', 'CKGMRU', 'CTSKBR', 'SINWUH', 'JOGKIX', 'KIXKNO', 'CKGKNO', 'MELMRU', 'HANOOL', 'KNOOOL', 'HKTIKA', 'HKTICN', 'PEKREP', 'LPQTPE', 'PEKSYD', 'PERTWU', 'KBRXIY', 'DMKICN', 'IKAPEK', 'OOLTPE', 'MYYPER', 'PEKSBW', 'KHHMEL', 'OOLPNH', 'CGKDEL', 'CNXKIX', 'BDOCTS', 'MRUSYD', 'ICNJHB', 'BWNSYD', 'MELPVG', 'OOLTGG', 'KIXLPQ', 'KBRKTM', 'BTUPER', 'HGHSUB', 'HYDOOL', 'GOIKUL', 'IKAPEN', 'MRUPER', 'KTMTWU', 'KCHMEL', 'MRUSZX', 'CTUSGN', 'KIXMEL', 'CTSKNO', 'PERSIN', 'CNXTPE', 'ICNSDK', 'PERSBW', 'HGHMRU', 'PERTPE', 'CKGPNH', 'CGKTPE', 'ICNSYD', 'AORKIX', 'HGHTRZ', 'HNDMEL', 'CGKICN', 'DELJOG', 'CCUSYD', 'DPSTPE', 'CTUKCH', 'MRUPEK', 'DACHGH', 'PNHTPE', 'CTUMRU', 'SYDVTE', 'CTSSUB', 'SYDTPE', 'BKIPEK', 'KCHPER', 'CXRMEL', 'MELSGN', 'HGHKCH', 'HNDPEN', 'JOGTPE', 'MYYXIY', 'ICNVTE', 'CKGSYD', 'DMKSYD', 'PERWUH', 'CTSKCH', 'DACPER', 'MELUTP', 'BKIHND', 'KIXLBU', 'SBWWUH', 'KNOPUS', 'IKATPE', 'PENWUH', 'DELJHB', 'CMBHGH', 'HDYMEL', 'JHBMEL', 'CTUMEL', 'SINTPE', 'HNDPNH', 'MRUPEN', 'CKGDPS', 'CGKXIY', 'OOLURT', 'CTUPEN', 'DMKHND', 'JEDMEL', 'SUBXIY', 'ICNTRZ', 'AORPER', 'TGGTPE', 'JHBSYD', 'PERXIY', 'PEKRGN', 'HGHSGN', 'CKGTGG', 'IKAMEL', 'CKGTWU', 'DPSICN', 'LGKPER', 'CEBPER', 'DELMYY', 'KCHMRU', 'PVGTGG', 'KOSPEK', 'DPSHGH', 'PEKSIN', 'HGHHKT', 'HNDIKA', 'PUSSYD', 'CTUSYD', 'DELKCH', 'LGKPEK', 'IKASGN', 'CNXPEK', 'CTUJHB', 'PUSTRZ', 'OOLREP', 'MELPEN', 'KIXSUB', 'SUBSYD', 'GOIMEL', 'CGKCKG', 'HKTTPE', 'MLEPVG', 'DMKPUS', 'MELWUH', 'BKIKTM', 'MYYSYD', 'COKKIX', 'CMBPER', 'MRUPVG', 'MRUOOL', 'DMKPVG', 'CTUHKT', 'HGHKNO', 'MLEPER', 'HKGMRU', 'KBRSYD', 'DMKHGH', 'CANMEL', 'HGHKBR', 'KNOMEL', 'DMKKIX', 'JOGKTM', 'DELSBW', 'AKLMRU', 'KCHTPE', 'CGKMEL', 'CEBMEL', 'BKISYD', 'HYDWUH', 'KNOPER', 'CMBMRU', 'PVGSIN', 'ICNIKA', 'PERSUB', 'AKLHGH', 'MELTGG', 'ICNKBV', 'MLEPEK', 'CGKJED', 'LOPTPE', 'BKIXIY', 'KTMPER', 'CTSDPS', 'DPSKTM', 'KIXMLE', 'CSXPER', 'JEDKNO', 'DACSYD', 'SGNXIY', 'LBUPER', 'ICNMAA', 'JHBPVG', 'MELREP', 'PEKTGG', 'CTULGK', 'HGHOOL']
    choices = [(choice, choice) for choice in ROUTE_CHOICES ]
    
    route =forms.ChoiceField(
        choices=choices,
        widget=forms.Select(
            attrs={
                "placeholder": "Route",
                "class": "form-control",
            }
        )
    )
            
    CHOICES = [(True, 'Yes'), (False, 'No')]
    available = forms.ChoiceField(
        choices=CHOICES,
        widget= forms.RadioSelect (
            
        ))
    class Meta:
        model = Flight
        fields = ['flight_name', 'flight_UID' , 'flight_start', 'flight_end','From','To' ,'route', 'available' ]
        
    def clean(self):
        cleaned_data = super().clean()
        flight_start = cleaned_data.get("flight_start")
        flight_end = cleaned_data.get("flight_end")
        if flight_start and flight_end:
            if flight_start >= flight_end:
                raise forms.ValidationError("Flight start must be less than flight end")
            
class CreateFlightReservationForm (ModelForm):
    travel_duration = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Travel Duration(You will stay there for how much days)",
                "class": "form-control",
            }
        ))
    CHOICES = [(True, 'Yes'), (False, 'No')]
    extra_baggage = forms.ChoiceField(
        choices=CHOICES,
        widget= forms.RadioSelect (
        ))
    
    choices_sales_channel = [('Internet', 'Internet') ,('Mobile','Mobile')]
    sales_channel =forms.ChoiceField(
        choices=choices_sales_channel,
        widget=forms.Select(
            attrs={
                "placeholder": "Sales channel",
                "class": "form-control",
            }
        )
    )
    
    CHOICE_ORIGIN = ['Greece', 'Turkey', 'Ghana', 'Kuwait', 'United Kingdom', 'United States', 'Brunei', 'Gibraltar', 'Argentina', 'Egypt', 'Nicaragua', 'Sweden', 'Mongolia', 'Oman', 'Tonga', 'Chile', 'Thailand', 'Slovakia', 'Kenya', 'Macau', 'Bulgaria', 'Guam', 'Paraguay', 'New Caledonia', 'Bhutan', 'Singapore', 'Taiwan', 'Malaysia', 'Mexico', 'Germany', 'Belarus', 'Brazil', 'India', 'Qatar', 'Russia', 'Portugal', 'Belgium', 'Norfolk Island', 'Netherlands', 'Ireland', 'Hungary', 'Italy', 'Sri Lanka', 'New Zealand', 'Papua New Guinea', 'Laos', 'Lebanon', 'Canada', 'Switzerland', 'RÃ©union', 'Panama', 'Hong Kong', 'Indonesia', 'South Africa', 'China', 'Estonia', 'South Korea', 'Austria', 'Timor-Leste', '(not set)', 'Mauritius', 'Pakistan', 'Tanzania', 'Tunisia', 'Maldives', 'Bangladesh', 'Myanmar (Burma)', 'Kazakhstan', 'Denmark', 'Colombia', 'Cyprus', 'Jordan', 'Israel', 'Czechia', 'Romania', 'Vanuatu', 'Philippines', 'Ukraine', 'Malta', 'United Arab Emirates', 'Afghanistan', 'Peru', 'Algeria', 'Spain', 'Iraq', 'Saudi Arabia', 'Iran', 'Nepal', 'Norway', 'Seychelles', 'France', 'Finland', 'Svalbard & Jan Mayen', 'Croatia', 'Bahrain', 'Cambodia', 'Poland', 'Australia', 'Vietnam', 'Japan', 'Slovenia', 'Solomon Islands', 'Guatemala', 'Czech Republic']
    choices_orign = [(choice, choice) for choice in CHOICE_ORIGIN]
    origin =forms.ChoiceField(
        choices=choices_orign,
        widget=forms.Select(
            attrs={
                "placeholder": "Origin",
                "class": "form-control",
            }
        )
    )
    CHOICE_TYPE =['RoundTrip', 'CircleTrip', 'OneWay']
    choices_type = [(choice, choice) for choice in CHOICE_TYPE]
    trip_type =forms.ChoiceField(
        choices=choices_type,
        widget=forms.Select(
            attrs={
                "placeholder": "Origin",
                "class": "form-control",
            }
        )
    )
    meal = forms.ChoiceField(
        choices=CHOICES,
        widget= forms.RadioSelect (
        ))
    
    preffered_seat = forms.ChoiceField(
        choices=CHOICES,
        widget= forms.RadioSelect (
        ))
    number_of_chair = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Number of chair (write 0 if random)",
                "class": "form-control",
            }
        ))
        
    number_of_chairs_to_reserve = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Number of chairs to reserve",
                "class": "form-control",
            }
        ))

    class Meta:
        model = ReservationFlight
        fields = ['travel_duration','sales_channel','number_of_chairs_to_reserve','origin','trip_type', 'extra_baggage' , 'meal', 'preffered_seat','number_of_chair']
    