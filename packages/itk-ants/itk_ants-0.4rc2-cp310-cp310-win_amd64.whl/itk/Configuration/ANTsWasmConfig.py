depends = ('ITKPyBase', 'ITKTransform', 'ITKRegistrationMethodsv4', 'ITKImageLabel', 'ITKImageGrid', 'ITKIOTransformBase', 'ITKIOImageBase', 'ITKCommon', 'ITKBinaryMathematicalMorphology', )
templates = (  ('ANTsRegistration', 'itk::ANTsRegistration', 'itkANTsRegistrationDISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >, double'),
  ('ANTsRegistration', 'itk::ANTsRegistration', 'itkANTsRegistrationDIUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >, double'),
  ('ANTsRegistration', 'itk::ANTsRegistration', 'itkANTsRegistrationDIUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >, double'),
  ('ANTsRegistration', 'itk::ANTsRegistration', 'itkANTsRegistrationDIF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >, double'),
  ('ANTsRegistration', 'itk::ANTsRegistration', 'itkANTsRegistrationDID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >, double'),
  ('ANTsRegistration', 'itk::ANTsRegistration', 'itkANTsRegistrationDISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >, double'),
  ('ANTsRegistration', 'itk::ANTsRegistration', 'itkANTsRegistrationDIUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >, double'),
  ('ANTsRegistration', 'itk::ANTsRegistration', 'itkANTsRegistrationDIUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >, double'),
  ('ANTsRegistration', 'itk::ANTsRegistration', 'itkANTsRegistrationDIF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >, double'),
  ('ANTsRegistration', 'itk::ANTsRegistration', 'itkANTsRegistrationDID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >, double'),
  ('ANTsRegistration', 'itk::ANTsRegistration', 'itkANTsRegistrationDISS4', True, 'itk::Image< signed short,4 >, itk::Image< signed short,4 >, double'),
  ('ANTsRegistration', 'itk::ANTsRegistration', 'itkANTsRegistrationDIUC4', True, 'itk::Image< unsigned char,4 >, itk::Image< unsigned char,4 >, double'),
  ('ANTsRegistration', 'itk::ANTsRegistration', 'itkANTsRegistrationDIUS4', True, 'itk::Image< unsigned short,4 >, itk::Image< unsigned short,4 >, double'),
  ('ANTsRegistration', 'itk::ANTsRegistration', 'itkANTsRegistrationDIF4', True, 'itk::Image< float,4 >, itk::Image< float,4 >, double'),
  ('ANTsRegistration', 'itk::ANTsRegistration', 'itkANTsRegistrationDID4', True, 'itk::Image< double,4 >, itk::Image< double,4 >, double'),
)
factories = ()
