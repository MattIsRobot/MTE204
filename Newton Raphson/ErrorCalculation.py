def calcError(lastEstimate, currentEstimate):
    if lastEstimate == None: 
        return "---"
    return f"{(abs(currentEstimate-lastEstimate)/currentEstimate)*100}%"

