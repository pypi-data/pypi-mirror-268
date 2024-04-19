/*
pyodide-mkdocs-theme
Copyleft GNU GPLv3 🄯 2024 Frédéric Zinelli

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.
If not, see <https://www.gnu.org/licenses/>.
*/



/**Prepare the runtime python environment:
 *  - Save the current code in the editor to LocaleStorage
 *  - Refresh the basic functionalities
 *  - Refresh any HDR content in the environment
 *  - Refresh any exclusion logistic, by defining extra functions in the environment
 *  - Returns the modified code, with the active terminal
 */
async function setupRuntimeAndTerminal(editorName) {

    // Extract the user's full code (possibly with public tests):
    let aceCode = await ace.edit(editorName).getSession().getValue();

    // save before anything else, in case an error occur somewhere...
    _save(editorName, aceCode)


    // Build the default configuration options to use to run the user's code:
    const options = buildOptionsForPyodideRun(editorName)

    // Refresh the pyodide environment, before running anything, and pause it (so that
    // the ">>>" are not displayed during the executions):
    const terminal = await setupOrGetTerminalAndPyEnv("term_" + editorName, true);
    terminal.pause()
    terminal.clear()
    terminal.echo(CONFIG.lang.runScript.msg)
    await sleep()     // Enforce UI refresh

    // Run before clearing the terminal, in case someone forgot a print:
    setupStdIO()
    let stdErr=''
    try{
        await runHdrContent(editorName, options, terminal)
    }catch(err){
        stdErr = generateErrorLog(err, "", false)
    }finally{
        let someMsg = (getFullStdIO()||"") + stdErr
        if(someMsg) terminal.echo(someMsg)
    }

    return [aceCode, terminal, options]
}



/**Actions performed once all the running code steps have been completed.
 *
 * This function MUST be always executed, whatever happened before, even for JS errors,
 * otherwise the terminal would stay locked. So its call must be in a try/finally clause.
 *
 * @terminal :   the currently "active" (paused) terminal.
 * @stdErr :     message that got already displayed in the terminal, or empty string id no error.
 * @successMsg : only used for validation tests. If they succeeded, this string won't be empty.
 * */
function tearDownRuntimeAndTerminal(terminal, stdErr, finalMsg="") {
    jsLogger("[Teardown] -", JSON.stringify(stdErr))

    if(!stdErr || finalMsg){
        terminal.echo(finalMsg || CONFIG.lang.successMsg.msg)
    }
    terminal.resume()
}






/**Applique c ^ key à chaque nombre de text
 * (Nota: 43960 = 0b1010101010101010)
 * */
const decrypt_string=(text, key = 43960) =>{
    if(!CONFIG.encryptCorrectionsAndRems) return text
    return text.split('.').map(c=>String.fromCodePoint( key ^ +c )).join('')
}







/**Extract the content of the header code for the given editorName, and run its content
 * into pyodide environment.
 * */
async function runHdrContent(editorName, options, terminal) {
    const headerContent = securedExtraction(editorName, CONFIG.ideProp.hdrContent)
    if(headerContent){
        await installAndImportMissingModules(headerContent, options, terminal)
        pyodide.runPython(headerContent)
    }
}



function getAttemptsLeft(editorName){
    return securedExtraction(editorName, CONFIG.ideProp.attemptsLeft)
}




function updateIdeCounter(editorName){

    let nAttempts = getAttemptsLeft(editorName) - 1
    securedUpdate(editorName, "attempts_left", nAttempts)
    const encrypted = securedExtraction(editorName, CONFIG.ideProp.encrypted)

    // Update the GUI counter if needed
    if (Number.isFinite(nAttempts) && nAttempts >= 0 && encrypted){
        const cntElement = document.getElementById("compteur_" + editorName)
        cntElement.textContent = nAttempts
    }
    return nAttempts
}



/**Reveal the solution+rem if still encrypted and either success or no attempts left
 * */
function unhideSolutionAndRem(editorName, nAttemptsLeft=Infinity, success=true){

    let encrypted = securedExtraction(editorName, CONFIG.ideProp.encrypted)
    let something = securedExtraction(editorName, CONFIG.ideProp.corrRemMask)

    if(something && encrypted && (success || nAttemptsLeft < 1)){
        const sol_div = document.getElementById("solution_" + editorName)
        const corr_content = decrypt_string(sol_div.innerHTML)
        sol_div.innerHTML = corr_content
        sol_div.classList = []
        mathJaxUpdate()                                 // Enforce formatting, if ever...
        securedUpdate(editorName, 'encrypted', false)   // Forbid coming back here
        return true
    }
    return false
}





/**Build an additional final message to add after an error message (which has already been
 * displayed in the terminal.
 * */
function enhanceFailureMsg(editorName, stdErr){
    let out = getSolRemTxt(editorName, false)
    return out
}



/**Build the full success message
 * */
function buildSuccessMessage(editorName){
    const emo = choice(CONFIG.MSG.successEmojis)
    let info = getSolRemTxt(editorName, true)
    return `${ success(CONFIG.lang.successHead.msg) } ${ emo } ${ CONFIG.lang.successHeadExtra.msg }${ info }`
}



/**Build the message for the terminal, announcing that correction and remarks becoming available.
 * */
function getSolRemTxt(editorName, isSuccess){
    const CorrRemMask = securedExtraction(editorName, CONFIG.ideProp.corrRemMask)
    if(!CorrRemMask) return ""

    const msg=[]
    if(isSuccess) msg.push("\n"+CONFIG.lang.successTail.msg)
    else          msg.push( failure(CONFIG.lang.failHead.msg) )

    const sentence = []
    if(CorrRemMask&1)  sentence.push(CONFIG.lang.revealCorr.msg)
    if(CorrRemMask==3) sentence.push(CONFIG.lang.revealJoin.msg)
    if(CorrRemMask&2)  sentence.push(CONFIG.lang.revealRem.msg)

    if(!isSuccess){
        if(sentence.length)   sentence[0] = _.capitalize(sentence[0])

        if(CorrRemMask&2)     sentence.push(CONFIG.lang.failTail.plural)
        else if(CorrRemMask)  sentence.push(CONFIG.lang.failTail.msg)
    }

    msg.push(...sentence)
    msg[msg.length-1] += "."

    return msg.join(' ')
}
