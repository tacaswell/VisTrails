;###############################################################################
;##
;## Copyright (C) 2011-2014, NYU-Poly.
;## Copyright (C) 2006-2011, University of Utah. 
;## All rights reserved.
;## Contact: vistrails@sci.utah.edu
;##
;## This file is part of VisTrails.
;##
;## "Redistribution and use in source and binary forms, with or without 
;## modification, are permitted provided that the following conditions are met:
;##
;##  - Redistributions of source code must retain the above copyright notice, 
;##    this list of conditions and the following disclaimer.
;##  - Redistributions in binary form must reproduce the above copyright 
;##    notice, this list of conditions and the following disclaimer in the 
;##    documentation and/or other materials provided with the distribution.
;##  - Neither the name of the University of Utah nor the names of its 
;##    contributors may be used to endorse or promote products derived from 
;##    this software without specific prior written permission.
;##
;## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
;## AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
;## THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR 
;## PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR 
;## CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
;## EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
;## PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
;## OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
;## WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
;## OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
;## ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
;##
;###############################################################################
[Setup]
AppName=VisTrails
AppVerName=VisTrails 2.1.2
WizardImageFile=resources\images\vistrails_icon.bmp
WizardImageStretch=false
WizardImageBackColor=$009D5942
DefaultDirName={code:CustomAppDir}\VisTrails
SetupIconFile=resources\icons\vistrails_install2.ico
DefaultGroupName=VisTrails
InfoAfterFile=Input\releaseNotes.txt
PrivilegesRequired=none
RestartIfNeededByRun=false
ChangesAssociations=true
LicenseFile=Input\license.txt
OutputBaseFilename=vistrails-setup

[Files]
Source: C:\Python27\w9xpopen.exe; DestDir: {app}\Python27
Source: C:\Python27\LICENSE.txt; DestDir: {app}\Python27
Source: C:\Python27\*.exe; DestDir: {app}\Python27
;Source: C:\Python27\qt.conf; DestDir: {app}\Python27
Source: C:\Python27\README.txt; DestDir: {app}\Python27
Source: C:\Python27\DLLs\*; DestDir: {app}\Python27\DLLs
Source: C:\Python27\include\*; DestDir: {app}\Python27\include
Source: C:\Python27\Lib\*; DestDir: {app}\Python27\Lib; Flags: recursesubdirs
Source: C:\Python27\libs\*; DestDir: {app}\Python27\libs
Source: C:\Python27\Scripts\*; DestDir: {app}\Python27\Scripts
Source: C:\Python27\tcl\*; DestDir: {app}\Python27\tcl; Flags: recursesubdirs
Source: C:\Python27\Tools\*; DestDir: {app}\Python27\Tools; Flags: recursesubdirs
Source: ..\..\examples\*; DestDir: {app}\examples; Components: examples; Flags: recursesubdirs
Source: ..\..\scripts\*; DestDir: {app}\scripts; Flags: recursesubdirs
Source: ..\..\vistrails\*; DestDir: {app}\vistrails; Flags: recursesubdirs
Source: ..\..\extensions\*; DestDir: {app}\extensions; Flags: recursesubdirs
Source: Input\unzip.exe; DestDir: {app}
Source: Input\zip.exe; DestDir: {app}
Source: Input\git.exe; DestDir: {app}
Source: Input\tar.exe; DestDir: {app}
Source: Input\runvistrails.py; DestDir: {app}
Source: Input\*.dll; DestDir: {app}
Source: Input\license.txt; DestDir: {app}
Source: Input\vcredist_x86.exe; DestDir: {tmp}; Flags: deleteafterinstall
Source: Input\VisTrails.pdf; DestDir: {app}\doc; Components: usersguide
Source: Input\qt.conf; DestDir: {app}\Python27

;;;; ------- QT LIBS ------- ;;;;
;;;; -- Already included in PyQt4 binary ---- ;;;;
;Source: D:\Qt\4.6.2\bin\*.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\phonon4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\Qt3Support4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtAssistantClient4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtCLucene4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtCore4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtDesigner4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtDesignerComponents4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtGui4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtHelp4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtMultimedia4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtNetwork4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtOpenGL4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtScript4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtScriptTools4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtSql4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtSvg4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtTest4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtWebKit4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtXml4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\bin\QtXmlPatterns4.dll; DestDir: {app}\vistrails
;Source: D:\Qt\4.6.3\plugins\iconengines\*; DestDir: {app}\vistrails\Python26\plugins\iconengines
;Source: D:\Qt\4.6.3\plugins\imageformats\*; DestDir: {app}\vistrails\Python26\plugins\imageformats
;Source: Input\qt.conf; DestDir: {app}\vistrails\Python26
Source: Input\x86\python27.dll; DestDir: {app}
Source: Input\x86\python27.dll; DestDir: {app}\Python27
Source: C:\Users\vistrails\src\vtk\vtk-5.10.1\build\bin\Release\*.dll; DestDir: {app}
Source: C:\Users\vistrails\src\vtk\vtk-5.10.1\build\bin\Release\*.pyd; DestDir: {app}
;Source: D:\src\VTKbuild\Wrapping\Python\vtk\*; DestDir: {app}\vistrails\vtk; Flags: recursesubdirs

;-->Source: I:\emanuele\src\netcdf-3.6.1\src\lib\*.dll; DestDir: {app}\vistrails
;;;; --------    ALPS FILES    ----------;;;;
Source: Input\x86\alps_libs\*; DestDir: {app}; Flags: recursesubdirs
;;;; --------    ITK FILES    ----------;;;;
;Source: E:\src\itk\Wrapping\WrapITK\Python\Release\*; DestDir: {app}; Flags: recursesubdirs
;Source: E:\src\itk\Wrapping\WrapITK\Python\Release\itkExtras\*; DestDir: {app}\itkExtras; Flags: recursesubdirs
;Source: E:\src\itk\Wrapping\WrapITK\Python\Release\Configuration\*; DestDir: {app}\Configuration; Flags: recursesubdirs
;Source: E:\src\itk\bin\Release\*.dll; DestDir: {app}
;Source: E:\src\itk\bin\Release\*.pyd; DestDir: {app}
;Source: E:\src\itk\bin\Release\*.py; DestDir: {app}
;;;; --------- END OF ITK FILES --------- ;;;;
Source: C:\Users\vistrails\src\fftw-3.3.3-dll32\libfftw3-3.dll; DestDir: {app}
Source: C:\Users\vistrails\src\hdf5-1.8.4-32bit-VS2008-IVF101\*; DestDir: {app}\libsrc\hdf5-1.8.4-32bit-VS2008-IVF101; Flags: recursesubdirs

[Dirs]
;Name: {%HOMEDRIVE}\{%HOMEPATH}\.vistrails
Name: {app}\vistrails
;;Name: {app}\Configuration
;;Name: {app}\itkExtras
Name: {app}\examples; Components: examples; Tasks: 
Name: {app}\extensions; Components: extensions; Tasks:
Name: {app}\doc; Components: usersguide; Tasks:  
Name: {app}\scripts
Name: {app}\scripts\gen_vtk_examples
Name: {app}\libsrc
Name: {app}\Python27
Name: {app}\Python27\DLLs
Name: {app}\Python27\include
Name: {app}\Python27\Lib
Name: {app}\Python27\libs
Name: {app}\Python27\Scripts
Name: {app}\Python27\sip
Name: {app}\Python27\tcl
Name: {app}\Python27\Tools
[Components]
Name: main; Description: Main Files; Types: full compact custom; Flags: fixed
Name: examples; Description: Example Files; Types: full
Name: extensions; Description: Extension Files; Types: full
Name: usersguide; Description: User's Guide PDF document; Types: full

[Icons]
Name: {group}\VisTrails; Filename: {app}\Python27\python.exe; WorkingDir: {app}; IconFilename: {app}\vistrails\gui\resources\images\vistrails_icon_small.ico; IconIndex: 0; Components: ; Parameters: vistrails\run.py
Name: {commondesktop}\VisTrails; Filename: {app}\Python27\python.exe; WorkingDir: {app}; IconFilename: {app}\vistrails\gui\resources\images\vistrails_icon_small.ico; IconIndex: 0; Parameters: vistrails\run.py; Components: main; Tasks: desktopicon
Name: {group}\Uninstall VisTrails; Filename: {uninstallexe}
Name: {group}\VisTrails.pdf; Filename: {app}\doc\VisTrails.pdf; Components: usersguide
[Tasks]
Name: desktopicon; Description: Create a &desktop icon; GroupDescription: Additional icons:; Components: main
Name: desktopicon\common; Description: For all users; GroupDescription: Additional icons:; Components: main; Flags: exclusive
Name: desktopicon\user; Description: For the current user only; GroupDescription: Additional icons:; Components: main; Flags: exclusive unchecked
Name: quicklaunchicon; Description: Create a &Quick Launch icon; GroupDescription: Additional icons:; Components: main; Flags: unchecked
Name: associatefiles; Description: Associate *.vt files with VisTrails; GroupDescription: File Association:; Components: main
[_ISTool]
LogFile=Output\build.log
LogFileAppend=false
[Registry]
Root: HKCR; Subkey: .vt; ValueType: string; ValueData: VisTrailsFile; Flags: uninsdeletevalue; Tasks: associatefiles
Root: HKCR; Subkey: VisTrailsFile; ValueType: string; ValueData: VisTrails File; Flags: uninsdeletekey; Tasks: associatefiles
Root: HKCR; Subkey: VisTrailsFile\DefaultIcon; ValueType: string; ValueData: {app}\vistrails\gui\resources\images\vistrails_icon_small.ico; Tasks: associatefiles; Flags: uninsdeletekey
Root: HKCR; Subkey: VisTrailsFile\shell\open\command; ValueType: string; ValueData: """{app}\Python27\python.exe"" ""{app}\runvistrails.py"" ""{app}\Python27\python.exe"" ""{app}\vistrails\run.py"" ""{app}"" ""%1"""; Tasks: associatefiles; Flags: uninsdeletekey
Root: HKCR; Subkey: .vtl; ValueType: string; ValueData: VisTrailsFile; Flags: uninsdeletevalue; Tasks: associatefiles
[InstallDelete]
Name: {app}\dot.exe; Type: files
Name: {app}\freetype6.dll; Type: files
Name: {app}\jpeg.dll; Type: files
Name: {app}\libexpat.dll; Type: files
Name: {app}\libexpatw.dll; Type: files
Name: {app}\png.dll; Type: files
Name: {app}\z.dll; Type: files
Name: {app}\zlib1.dll; Type: files
Name: {app}\Python27; Type: filesandordirs
Name: {app}\*.pyd; Type: files
Name: {app}\dgnlib.dll; Type: files
Name: {app}\_Xdmf.dll; Type: files
Name: {app}\geotiff.dll; Type: files
Name: {app}\libmysql.dll; Type: files
Name: {app}\vistrails; Type: filesandordirs
Name: {app}\vistrails\packages\gridfield; Type: filesandordirs
Name: {app}\lib\site-packages; Type: filesandordirs
[Run]
Filename: {tmp}\vcredist_x86.exe; Parameters: /Q; Components: ; Tasks: 


[ThirdPartySettings]
CompileLogFile=Output\build.log
CompileLogMethod=append

[PreCompile]
Name: "C:\Python27\python.exe"; Parameters: "C:\Users\vistrails\code\vistrails\dist\windows\Input\download_usersguide.py"; Flags: abortonerror cmdprompt

[PreCompile]
Name: "C:\Python27\python.exe"; Parameters: "-m compileall C:\Users\vistrails\code"; Flags: abortonerror cmdprompt

[Code]
var
	FinishedInstall: Boolean;
function CustomAppDir(Param: String): String;
begin
	if IsAdminLoggedOn then
		Result := ExpandConstant('{pf}')
	else
		Result := ExpandConstant('{userappdata}')
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
    FinishedInstall := True;
end;

procedure CurPageChanged(CurPageID: Integer);
begin
//  case CurPageID of
//    wpReady:
//    begin
//	  DeleteFile(ExpandConstant('{app}') + '\python27.dll');
//      oldPythonDir := ExpandConstant('{app}') + '\Python27';
//	  if DirExists(oldPythonDir) then
//	    DelTree(oldPythonDir, True, True, True);}
//	end;
//  end;
end;

procedure DeleteVCRedistRuntimeTemporaryFiles();
var
   i : Integer;
   byCounter : Byte;
   byDrive : Byte;
   strFile1, strFile2, strFile3 : String;
   strRootDrivePath : String;
   //totally there are 24 files to be deleted
   arrFiles : Array [1..24] Of String;
begin

   //We will check the following root drives
   //C, D, E, F, G, H, I, J, K, L, M
   For byCounter := 67 to 77 do
   Begin
      strRootDrivePath := Chr(byCounter) + ':\';
      arrFiles[1] := strRootDrivePath + 'vcredist.bmp';
      arrFiles[2] := strRootDrivePath + 'VC_RED.cab';
      arrFiles[3] := strRootDrivePath + 'VC_RED.MSI';

      //If these 3 files then we have found the right
      //drive in which the VC runtime files are extracted
      If (FileExists(arrFiles[1]) And
          FileExists(arrFiles[2]) And
          FileExists(arrFiles[3])) Then
      Begin

          arrFiles[4] := strRootDrivePath + 'eula.1028.txt';
          arrFiles[5] := strRootDrivePath + 'eula.1031.txt';
          arrFiles[6] := strRootDrivePath + 'eula.1033.txt';
          arrFiles[7] := strRootDrivePath + 'eula.1036.txt';
          arrFiles[8] := strRootDrivePath + 'eula.1040.txt';
          arrFiles[9] := strRootDrivePath + 'eula.1041.txt';
          arrFiles[10] := strRootDrivePath + 'eula.1042.txt';
          arrFiles[11] := strRootDrivePath + 'eula.2052.txt';
          arrFiles[12] := strRootDrivePath + 'eula.3082.txt';
          arrFiles[13] := strRootDrivePath + 'globdata.ini';
          arrFiles[14] := strRootDrivePath + 'install.exe';
          arrFiles[15] := strRootDrivePath + 'install.ini';
          arrFiles[16] := strRootDrivePath + 'install.res.1028.dll';
          arrFiles[17] := strRootDrivePath + 'install.res.1031.dll';
          arrFiles[18] := strRootDrivePath + 'install.res.1033.dll';
          arrFiles[19] := strRootDrivePath + 'install.res.1036.dll';
          arrFiles[20] := strRootDrivePath + 'install.res.1040.dll';
          arrFiles[21] := strRootDrivePath + 'install.res.1041.dll';
          arrFiles[22] := strRootDrivePath + 'install.res.1042.dll';
          arrFiles[23] := strRootDrivePath + 'install.res.2052.dll';
          arrFiles[24] := strRootDrivePath + 'install.res.3082.dll';

          For i := 1 to 24 Do
          Begin
            DeleteFile(arrFiles[i]);
          End;

          //Now that we have found and deleted all the files
          //we will break
          Break;
      End;
   End;
End;

procedure DeinitializeSetup();
var
  qvtk: String;
begin
  if FinishedInstall then begin
      qvtk := ExpandConstant('{app}') + '\vistrails\packages\spreadsheet\widgets\QVTKWidget';
	  if DirExists(qvtk) then
		DelTree(qvtk, True, True, True);
  end;
  DeleteVCRedistRuntimeTemporaryFiles();
end;

[InnoIDE_Settings]
LogFile=Output\build.log
LogFileOverwrite=false

[InnoIDE_PreCompile]
Name: C:\Python27\python.exe; Parameters: C:\Users\vistrails\code\vistrails\dist\windows\Input\download_usersguide.py; Flags: AbortOnError CmdPrompt; 
