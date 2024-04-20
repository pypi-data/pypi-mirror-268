StiHandler.prototype.process = function (args, callback) {
    if (args) {
        if (args.event === 'OpenReport')
            return null;
        
        if (args.event === 'BeginProcessData' || args.event === 'EndProcessData') {
            if (!this.databases.includes(args.database))
                return null;
            
            args.preventDefault = true;
        }

        if (callback)
            args.async = true;

        let command = {};
        for (let p in args) {
            if (p === 'report' && args.report) command.report = args.report.isRendered ? args.report.saveDocumentToJsonString() : args.report.saveToJsonString();
            else if (p === 'settings' && args.settings) command.settings = JSON.stringify(args.settings);
            else if (p === 'data') command.data = Stimulsoft.System.Convert.toBase64String(args.data);
            else if (p === 'variables') command[p] = this.getVariables(args[p]);
            else if (p == 'viewer') continue;
            else command[p] = args[p];
        }
        
        let sendText = Stimulsoft.Report.Dictionary.StiSqlAdapterService.encodeCommand(command);
        let callback2 = function (args2) {
            if (args2.report) args.report = args2.report;
            if (args2.settings) Stimulsoft.handler.copySettings(args2.settings, args.settings);
            if (args2.fileName) args.fileName = args2.fileName;
            
            if (!Stimulsoft.System.StiString.isNullOrEmpty(args2.notice))
                Stimulsoft.System.StiError.showError(args2.notice, true, args2.success);
            if (callback) callback(args2);
        }
        Stimulsoft.handler.send(sendText, callback2);
    }
}

StiHandler.prototype.send = function (data, callback) {
    let request = new XMLHttpRequest();
    try {
        let csrftoken = '{csrf_token}' || Stimulsoft.handler.getCookie('csrftoken');
        request.open('post', this.url, true);
        request.setRequestHeader('Cache-Control', 'no-cache, no-store, must-revalidate');
        request.setRequestHeader('Cache-Control', 'max-age=0');
        request.setRequestHeader('Pragma', 'no-cache');
        request.setRequestHeader('X-CSRFToken', csrftoken);
        request.timeout = this.timeout * 1000;
        request.onload = function () {
            if (request.status === 200) {
                let responseText = request.responseText;
                request.abort();

                try {
                    let args = Stimulsoft.Report.Dictionary.StiSqlAdapterService.decodeCommandResult(responseText);
                    if (args.report) {
                        let json = args.report;
                        args.report = new Stimulsoft.Report.StiReport();
                        args.report.load(json);
                    }

                    callback(args);
                } catch (e) {
                    Stimulsoft.System.StiError.showError(e.message);
                }
            } else {
                Stimulsoft.System.StiError.showError('Server response error: [' + request.status + '] ' + request.statusText);
            }
        };
        request.onerror = function (e) {
            let errorMessage = 'Connect to remote error: [' + request.status + '] ' + request.statusText;
            Stimulsoft.System.StiError.showError(errorMessage);
        };
        request.send(data);
    } catch (e) {
        let errorMessage = 'Connect to remote error: ' + e.message;
        Stimulsoft.System.StiError.showError(errorMessage);
        request.abort();
    }
}

StiHandler.prototype.getCookie = function (name) {
    let matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

StiHandler.prototype.setOptions = function () {
    StiOptions.WebServer.timeout = this.timeout;
    StiOptions.WebServer.encryptData = this.encryptData;
    StiOptions.WebServer.passQueryParametersToReport = this.passQueryParametersToReport;
    StiOptions.WebServer.checkDataAdaptersVersion = this.checkDataAdaptersVersion;
    StiOptions.Engine.escapeQueryParameters = this.escapeQueryParameters;
}

StiHandler.prototype.isNullOrEmpty = function (value) {
    return value == null || value === '' || value === undefined;
}

StiHandler.prototype.getVariables = function (variables) {
    if (variables) {
        for (let variable of variables) {
            if (variable.type === 'DateTime' && variable.value != null)
                variable.value = variable.value.toString('YYYY-MM-DD HH:mm:SS');
        }
    }

    return variables;
}

StiHandler.prototype.copySettings = function (from, to) {
    for (let key in from) {
        if (to.hasOwnProperty(key) && typeof to[key] != 'object' && typeof to[key] != 'function' && typeof from[key] == typeof to[key])
            to[key] = from[key];
    }
}

function StiHandler() {
    this.url = {url};
    this.timeout = {timeout};
    this.encryptData = {encryptData};
    this.passQueryParametersToReport = {passQueryParametersToReport};
    this.checkDataAdaptersVersion = {checkDataAdaptersVersion};
    this.escapeQueryParameters = {escapeQueryParameters};
    this.databases = {databases};
    this.frameworkType = 'Python';
    this.setOptions();
}

setTimeout(function () {
    Stimulsoft.handler = new StiHandler();
})
