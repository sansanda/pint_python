#source: https://pint.readthedocs.io/en/stable/tutorial.html
#Tutorial
#Follow the steps below and learn how to use Pint to track physical quantities and perform unit conversions in Python.

import pint
ureg = pint.UnitRegistry()
distance = 24 * ureg.meter
print(distance)
print(distance.units)
print(distance.magnitude)
print(distance.dimensionality)

time = 8 * ureg.seconds
print(time)

speed = distance/time
speed.ito('inch/minute')

print(speed)

speed.ito('meter/seconds')

print(speed)

#Simplifying units
#Sometimes, the magnitude of the quantity will be very large or very small. The method to_compact() can adjust the units to make a quantity more human-readable:

wavelength = 1550 * ureg.nm
frequency = (ureg.speed_of_light / wavelength).to('Hz')
print(frequency)
#193414489032258.03 hertz
print(frequency.to_compact())
#193.414489032... terahertz

#There are also methods to_base_units() and ito_base_units() which automatically convert to the reference units with the correct dimensionality:

height = 5.0 * ureg.foot + 9.0 * ureg.inch
print(height)
#5.75 foot
print(height.to_base_units())
#1.752... meter
print(height)
#5.75 foot
height.ito_base_units()
print(height)
#1.752... meter

#There are also methods to_reduced_units() and ito_reduced_units() which perform a simplified dimensional reduction,
# combining units with the same dimensionality but otherwise keeping your unit definitions intact.

density = 1.4 * ureg.gram / ureg.cm**3
volume = 10*ureg.cc
mass = density*volume
print(mass)
#14.0 cubic_centimeter * gram / centimeter ** 3
print(mass.to_reduced_units())
#14.0 gram
print(mass)
#14.0 cubic_centimeter * gram / centimeter ** 3
mass.ito_reduced_units()
print(mass)
#14.0 gram

print("\nSTRING PARSING\nSTRING PARSING\nSTRING PARSING\n")
#String parsing
#Pint includes powerful string parsing for identifying magnitudes and units. In many cases, units can be defined as strings:

print(2.54 * ureg('centimeter'))
#<Quantity(2.54, 'centimeter')>
#or using the Quantity constructor:

Q_ = ureg.Quantity
q = Q_(2.54, 'centimeter')
print(q)
#<Quantity(2.54, 'centimeter')>
#Numbers are also parsed, so you can use an expression:

print(ureg('2.54 * centimeter'))
#<Quantity(2.54, 'centimeter')>
q = Q_('2.54 * centimeter')
print(q)
#<Quantity(2.54, 'centimeter')>
#or leave out the * altogether:

q = Q_('2.54cm')
print(q)
#<Quantity(2.54, 'centimeter')>
#This enables you to build a simple unit converter in 3 lines:

user_input = '2.54 * centimeter to inch'
src, dst = user_input.split(' to ')
q = Q_(src).to(dst)
print(q)
#<Quantity(1.0, 'inch')>
#Strings containing values can be parsed using the ureg.parse_pattern() function. A format-like string with the units defined in it is used as the pattern:

input_string = '10 feet 10 inches'
pattern = '{feet} feet {inch} inches'
l = ureg.parse_pattern(input_string, pattern)
print(l)
#[<Quantity(10.0, 'foot')>, <Quantity(10.0, 'inch')>]
#To search for multiple matches, set the many parameter to True. The following example also demonstrates how the parser is able to find matches in amongst filler characters:

input_string = '10 feet - 20 feet ! 30 feet.'
pattern = '{feet} feet'
l = ureg.parse_pattern(input_string, pattern, many=True)
print(l)
#[[<Quantity(10.0, 'foot')>], [<Quantity(20.0, 'foot')>], [<Quantity(30.0, 'foot')>]]
#The full power of regex can also be employed when writing patterns:

input_string = "10` - 20 feet ! 30 ft."
pattern = r"{feet}(`| feet| ft)"
l = ureg.parse_pattern(input_string, pattern, many=True)
print(l)
#[[<Quantity(10.0, 'foot')>], [<Quantity(20.0, 'foot')>], [<Quantity(30.0, 'foot')>]]
#Note that the curly brackets (``{}``) are converted to a float-matching pattern by the parser.

#This function is useful for tasks such as bulk extraction of units from thousands of uniform strings or even very large texts with units dotted around in no particular pattern.