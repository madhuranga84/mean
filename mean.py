def mean(num_list):
	#assert isinstance(num_list, list)
        #if len(num_list)==0:
                #raise Exception("The algebraic mean of an empty list is undefined...!, please provide a non-empty list.")


        try:
                return sum(num_list)/len(num_list)
        #except ZeroDivisionError as detail: #exception doesn't necessasirily named as detail, it can called anything like say, info
         #       msg = "Please provide a list of numbers rather than an empty string."

          #      raise ZeroDivisionError(detail.__str__() + "\n" + msg)
        except ZeroDivisionError:
                return 0

        except TypeError as detail:
                msg = "Please provide a list of numbers."
                raise TypeError(detail.__str__() + "\n" + msg)
