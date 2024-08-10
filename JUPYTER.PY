def minutes_to_hours(minutes):
  """Converts minutes to hours.

  Args:
    minutes: The number of minutes to convert.

  Returns:
    The equivalent number of hours as a float.
  """

  return minutes / 60

# Example usage:
minutes = 150
hours = minutes_to_hours(minutes)
print(f"{minutes} minutes is equal to {hours} hours")

OUTPUT
150 minutes is equal to 2.5 hours
